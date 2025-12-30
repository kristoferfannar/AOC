use crate::{
    day::{AocResult, Day, Type},
    load_input,
};

pub struct Day1;

impl Day for Day1 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);

        let mut part1 = 0;
        let mut curr = 50;
        let circle = 100;

        // part 1
        contents.lines().for_each(|l| {
            let dir = l.chars().nth(0).unwrap();
            let num: i32 = l[1..].parse().unwrap();

            match dir {
                'L' => {
                    curr = (curr - num) % circle;
                }
                'R' => {
                    curr = (curr + num) % circle;
                }
                _ => panic!("{dir} is not one of 'L', 'R'"),
            };

            if curr == 0 {
                part1 += 1;
            }
        });

        // part 2
        let mut part2 = 0;
        let mut curr: i64 = 50;

        contents.lines().for_each(|l| {
            let dir = l.chars().nth(0).unwrap();
            let num: i64 = l[1..].parse().unwrap();

            for _ in 0..num {
                curr = match dir {
                    'L' => curr - 1,
                    'R' => curr + 1,
                    _ => return (),
                };

                if curr % 100 == 0 {
                    part2 += 1;
                }
            }
        });

        Ok((part1.into(), part2.into()))
    }
}
