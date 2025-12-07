use std::error::Error;
use std::i32;

mod day;
use crate::day::Day;

import_day!(day_1);
import_day!(day_2);
import_day!(day_3);

fn run<D: Day>() -> Result<(), Box<dyn Error>> {
    let day = D::NUMBER;
    let sample = format!("{day:02}_sample.txt");
    let actual = format!("{day:02}_actual.txt");

    println!("sample: {:?}", D::solve(sample));
    println!("actual: {:?}", D::solve(actual));

    Ok(())
}

fn solve_day(day: i32) -> Result<(), Box<dyn Error>> {
    match day {
        1 => run::<Day1>()?,
        2 => run::<Day2>()?,
        3 => run::<Day3>()?,
        _ => panic!("unknown day"),
    };

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    solve_day(3)?;
    Ok(())
}
