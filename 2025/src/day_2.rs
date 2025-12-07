use crate::day::*;
use std::fs::File;
use std::io::Read;

pub struct Day2;

impl Day for Day2 {
    const NUMBER: i32 = 2;
    fn solve(path: String) -> Option<(i64, i64)> {
        let mut file = File::open(path).ok()?;
        let mut contents = String::new();
        file.read_to_string(&mut contents).ok()?;
        contents = contents.trim().to_string();

        let ranges = contents.split(',');

        let mut part1 = 0;

        ranges.for_each(|range| {
            let mut splits = range.splitn(2, '-');
            let first = splits.next().unwrap().parse::<i64>().unwrap();
            let second = splits.next().unwrap().parse::<i64>().unwrap();

            for i in first..=second {
                let num = i.to_string();

                let mid = num.len() / 2;
                let first_half = &num[..mid];
                let second_half = &num[mid..];

                if first_half == second_half {
                    part1 += i;
                }
            }
        });

        let mut part2 = 0;

        let ranges = contents.split(',');
        ranges.for_each(|range| {
            let mut splits = range.splitn(2, '-');
            let first = splits.next().unwrap().parse::<i64>().unwrap();
            let second = splits.next().unwrap().parse::<i64>().unwrap();

            for i in first..=second {
                let num = i.to_string();
                let len = num.len();

                let mut is_good = false;
                for j in 1..len {
                    if len % j == 0 {
                        let mut j_is_good = true;
                        for idx in 0..=(len - j * 2) {
                            let last = &num[idx..idx + j];
                            let curr = &num[idx + j..idx + j * 2];

                            if last != curr {
                                j_is_good = false;
                                break;
                            }
                        }

                        if j_is_good {
                            is_good = true;
                            break;
                        }
                    }
                }

                if is_good {
                    part2 += i;
                }
            }
        });

        return Some((part1.into(), part2.into()));
    }
}
