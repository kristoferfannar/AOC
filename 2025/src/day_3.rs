use crate::day::Day;
use std::fs::File;
use std::io::Read;

pub struct Day3;

impl Day3 {
    fn find_n_largest_in_bank(mut n: usize, bank: Vec<i64>) -> i64 {
        let mut curr_num: i64 = 0;
        let mut start_idx = 0;

        while n > 0 {
            let (idx, val) = bank[start_idx..bank.len() - n + 1]
                .iter()
                .enumerate()
                // return first index if multiple maxes are found
                .max_by_key(|&(i, v)| (v, -(i as i64)))
                .unwrap();

            // idx is shifted by start_idx
            start_idx += idx + 1;
            curr_num = curr_num * 10 + val;

            n -= 1;
        }

        curr_num
    }
}

impl Day for Day3 {
    const NUMBER: i32 = 3;
    fn solve(path: String) -> Option<(i64, i64)> {
        let mut f = File::open(path).ok()?;
        let mut contents = String::new();

        let mut part1: i64 = 0;
        let mut part2: i64 = 0;

        f.read_to_string(&mut contents).ok()?;

        let lines = contents.trim().split('\n');
        lines.for_each(|line| {
            let bank = line
                .trim()
                .chars()
                .map(|c| c.to_digit(10).unwrap().into())
                .collect::<Vec<i64>>();

            part1 += Self::find_n_largest_in_bank(2, bank);
        });

        // Part 2:
        let lines = contents.trim().split('\n');
        lines.for_each(|line| {
            let bank = line
                .trim()
                .chars()
                .map(|c| c.to_digit(10).unwrap().into())
                .collect::<Vec<i64>>();

            part2 += Self::find_n_largest_in_bank(12, bank);
        });

        Some((part1, part2))
    }
}
