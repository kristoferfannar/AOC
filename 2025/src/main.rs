use std::error::Error;
use std::fmt::Display;
use std::fs::File;
use std::i32;
use std::io::Read;

fn day_1(path: String) -> Option<(i64, i64)> {
    let mut f = File::open(path).ok()?;
    let mut contents = String::new();

    f.read_to_string(&mut contents).ok()?;

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

    Some((part1.into(), part2.into()))
}

fn day_2(path: String) -> Option<(i64, i64)> {
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

fn solve_day(day: i32) -> Result<(), Box<dyn Error>> {
    let sample = format!("{day:02}_sample.txt");
    let actual = format!("{day:02}_actual.txt");

    let func = match day {
        1 => day_1,
        2 => day_2,
        _ => panic!("unknown day"),
    };

    println!("sample: {:?}", func(sample));
    println!("actual: {:?}", func(actual));

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    solve_day(2)?;
    Ok(())
}
