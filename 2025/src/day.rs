#[macro_export]
macro_rules! import_day {
    ($mod:ident) => {
        mod $mod;
        use crate::$mod::*;
    };
}

#[macro_export]
macro_rules! load_input {
    ($typ:expr) => {{
        match $typ {
            Type::Sample => include_str!("sample.txt"),
            Type::Actual => include_str!("actual.txt"),
        }
    }};
}

pub trait Day {
    fn solve(typ: Type) -> Option<(i64, i64)>;
}

pub enum Type {
    Sample,
    Actual,
}
