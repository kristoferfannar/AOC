use crate::{
    day::{AocResult, Day, Type},
    load_input,
};
use anyhow::Context;

pub struct Day6;

impl Day for Day6 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);
        let mut part1 = 0;
        let mut part2 = 0;

        // part 1
        let mut lines: Vec<Vec<&str>> = contents
            .trim()
            .split("\n")
            .map(|line| line.split_whitespace().collect())
            .collect();

        let ops = lines.pop().context("missing operations")?;

        for i in 0..lines[0].len() {
            let mut total = match ops[i] {
                "*" => 1,
                "+" => 0,
                _ => panic!(),
            };

            for o in 0..lines.len() {
                let item: i64 = lines[o][i].parse().context("can't convert to int")?;

                match ops[i] {
                    "*" => total *= item,
                    "+" => total += item,
                    _ => panic!(),
                }
            }

            part1 += total
        }

        // part 2
        let mut lines: Vec<Vec<char>> = contents
            .trim_matches('\n')
            .split("\n")
            .map(|line| line.chars().collect())
            .collect();
        let ops = lines.pop().unwrap();

        #[derive(Clone, Debug)]
        enum Case {
            Mult,
            Add,
            Empty,
        }

        let mut prev_case = Case::Empty;
        let mut total: i64 = 0;
        for i in 0..ops.len() {
            let case = match ops[i] {
                ' ' => prev_case.clone(),
                '*' => {
                    part2 += total;
                    total = 1;
                    prev_case = Case::Mult;
                    Case::Mult
                }
                '+' => {
                    part2 += total;
                    total = 0;
                    prev_case = Case::Add;
                    Case::Add
                }
                _ => panic!(),
            };

            let mut num = String::new();
            for n_i in 0..lines.len() {
                num.push(lines[n_i][i]);
            }

            let num = num.trim();

            if num == "" {
                continue;
            }

            let val: i64 = num
                .parse()
                .with_context(|| format!("can't convert to int: {num:?}"))?;

            match case {
                Case::Mult => total *= val,
                Case::Add => total += val,
                _ => panic!(),
            }
        }

        part2 += total;

        Ok((part1, part2))
    }
}
