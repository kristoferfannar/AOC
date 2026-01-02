use std::collections::{HashMap, HashSet};

use crate::{
    day::{AocResult, Day, Type},
    load_input,
};
use anyhow::Context;

pub struct Day7;

impl Day for Day7 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);
        let mut part1 = 0;
        let mut part2 = 0;

        let mut tachyons = HashSet::<(usize, usize)>::new();

        let mut grid: Vec<Vec<char>> = contents
            .trim_matches('\n')
            .split("\n")
            .map(|line| line.chars().collect())
            .collect();

        // println!("grid: {:?}", grid);

        let start_idx = grid[0]
            .iter()
            .position(|&c| c == 'S')
            .context("Couldn't find 'S'")? as usize;

        let mut stack = vec![(0, start_idx)];

        while stack.len() > 0 {
            let (mut r, c) = stack.pop().unwrap();

            // println!("r={r}, c={c}, total={part1}");
            // for ele in &grid {
            //     let s: String = ele.iter().collect();
            //     println!("{}", s);
            // }
            // ();

            while r < grid.len() {
                if grid[r][c] == '^' {
                    let ele = (r, c);

                    if tachyons.contains(&ele) {
                        break;
                    }

                    tachyons.insert((r, c));
                    if c > 0 {
                        stack.push((r, c - 1));
                    }
                    if c < grid[r].len() - 1 {
                        stack.push((r, c + 1));
                    }
                    break;
                }

                // grid[r][c] = '|';

                r += 1;
            }
        }

        part1 = tachyons.len() as i64;

        // part 2
        let mut tallies = HashMap::<(usize, usize), i64>::new();

        // initialize all entries
        // start with:
        // - 1 point for each cell in the last row
        // - 0 points for each '^' cell
        for r in 0..grid.len() {
            for c in 0..grid[r].len() {
                let key = (r, c);
                if r == grid.len() - 1 {
                    tallies.insert(key, 1);
                } else if grid[r][c] == '^' {
                    tallies.insert(key, 0);
                }
            }
        }

        // start at the bottom and go up,
        // finding all initialized entries and seeing
        // which other entries they land on
        for r in (0..grid.len()).rev() {
            for c in 0..grid[0].len() {
                let key = (r, c);

                let val = match tallies.get(&key) {
                    Some(&v) => v,
                    None => continue,
                };

                for rr in (0..r).rev() {
                    if grid[rr][c] == 'S' {
                        part2 += val;
                    }
                    if grid[rr][c] == '^' {
                        break;
                    }
                    // wrapping sub is technically ok since we won't have that c value in our map
                    if let Some(left) = tallies.get_mut(&(rr, c.wrapping_sub(1))) {
                        *left += val;
                    }
                    if let Some(right) = tallies.get_mut(&(rr, c + 1)) {
                        *right += val;
                    }
                }
            }
        }

        Ok((part1, part2))
    }
}
