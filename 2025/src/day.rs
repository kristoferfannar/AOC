#[macro_export]
macro_rules! import_day {
    ($mod:ident) => {
        mod $mod;
        use crate::$mod::*;
    };
}

pub trait Day {
    const NUMBER: i32;
    fn solve(path: String) -> Option<(i64, i64)>;
}
