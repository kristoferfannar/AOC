use std::collections::HashSet;

use crate::{
    day::{AocResult, Day, Type},
    load_input,
};

pub struct Day4;

impl Day4 {
    fn get_neighbours(rows: usize, cols: usize, r: usize, c: usize) -> (Vec<usize>, Vec<usize>) {
        let mut nrs = vec![r];
        let mut ncs = vec![c];
        if r > 0 {
            nrs.push(r - 1);
        }
        if r < rows - 1 {
            nrs.push(r + 1);
        }
        if c > 0 {
            ncs.push(c - 1);
        }
        if c < cols - 1 {
            ncs.push(c + 1);
        }

        (nrs, ncs)
    }
}

impl Day for Day4 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);
        let mut part1 = 0;
        let mut part2 = 0;

        let mut lines: Vec<Vec<char>> = contents
            .trim()
            .split('\n')
            .map(|line| line.chars().collect())
            .collect();

        let rows = lines.len();
        let cols = lines[0].len();

        for r in 0..rows {
            for c in 0..cols {
                if lines[r][c] == '.' {
                    continue;
                }
                let mut ns = 0;
                let neighbors = Self::get_neighbours(rows, cols, r, c);
                let nrs = neighbors.0;
                let ncs = neighbors.1;

                for nr in nrs.iter() {
                    for nc in ncs.iter() {
                        if *nr == r && *nc == c {
                            continue;
                        }

                        if lines[*nr][*nc] != '.' {
                            ns += 1;
                        }
                    }
                }
                if ns < 4 {
                    part1 += 1;
                    lines[r][c] = 'x';
                }
            }
        }

        // part 2
        let mut lines: Vec<Vec<char>> = contents
            .trim()
            .split('\n')
            .map(|line| line.chars().collect())
            .collect();

        let mut found: HashSet<(usize, usize)> = HashSet::new();
        let mut curr: HashSet<(usize, usize)> = HashSet::new();
        let mut next: HashSet<(usize, usize)> = HashSet::new();

        for r in 0..rows {
            for c in 0..cols {
                if lines[r][c] == '@' {
                    curr.insert((r, c));
                }
            }
        }

        while curr.len() > 0 {
            for point in curr.iter() {
                let r = point.0;
                let c = point.1;

                if found.contains(point) {
                    continue;
                }

                let mut ns: Vec<(usize, usize)> = vec![];
                let neighbors = Self::get_neighbours(rows, cols, r, c);
                let nrs = neighbors.0;
                let ncs = neighbors.1;

                for nr in nrs.iter() {
                    for nc in ncs.iter() {
                        if *nr == r && *nc == c {
                            continue;
                        }

                        if lines[*nr][*nc] == '@' {
                            ns.push((*nr, *nc));
                        }
                    }
                }
                if ns.len() < 4 {
                    part2 += 1;
                    lines[r][c] = 'x';
                    found.insert((r, c));
                    next.extend(ns);
                }
            }
            curr = next.clone();
            next.clear();
        }

        Ok((part1, part2))
    }
}
