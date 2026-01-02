use std::error::Error;
use std::i32;

mod day;
use crate::day::{Day, Type};

import_day!(day_1);
import_day!(day_2);
import_day!(day_3);
import_day!(day_4);
import_day!(day_5);
import_day!(day_6);
import_day!(day_7);

fn run<D: Day>() -> Result<(), Box<dyn Error>> {
    println!("sample: {:?}", D::solve(Type::Sample));
    println!("actual: {:?}", D::solve(Type::Actual));

    Ok(())
}

fn solve_day(day: i32) -> Result<(), Box<dyn Error>> {
    match day {
        1 => run::<Day1>()?,
        2 => run::<Day2>()?,
        3 => run::<Day3>()?,
        4 => run::<Day4>()?,
        5 => run::<Day5>()?,
        6 => run::<Day6>()?,
        7 => run::<Day7>()?,
        _ => panic!("unknown day"),
    };

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    solve_day(7)?;
    Ok(())
}
