use anyhow::Context;

use crate::{
    day::{AocResult, Day, Type},
    load_input,
};

pub struct Day5;

impl Day for Day5 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);
        let mut part1 = 0;
        let mut part2 = 0;

        let mut lines = contents.trim().splitn(2, "\n\n");

        let line1 = lines.next().context("missing line")?;
        let line2 = lines.next().context("missing line")?;

        let mut first: Vec<(i64, i64)> = line1
            .split('\n')
            .map(|l| {
                let mut nums = l.splitn(2, '-');
                let min: i64 = nums.next().unwrap().parse().unwrap();
                let max: i64 = nums.next().unwrap().parse().unwrap();

                (min, max)
            })
            .collect();
        let second: Vec<i64> = line2.split('\n').map(|l| l.parse().unwrap()).collect();

        first.sort();

        // part 1
        for num in second {
            for (min, max) in first.iter() {
                if *min <= num && num <= *max {
                    part1 += 1;
                    break;
                }
            }
        }

        // part 2
        let mut v = Vec::<(i64, i64)>::new();
        let mut idx = 0;

        while idx < first.len() {
            let (min, mut mx) = first[idx];
            for (nmin, nmax) in first[idx + 1..].iter() {
                if mx < *nmin {
                    break;
                }

                mx = mx.max(*nmax);
                idx += 1;
            }

            v.push((min, mx));

            idx += 1;
        }

        for (min, max) in v {
            part2 += max - min + 1;
        }

        Ok((part1, part2))
    }
}
