use crate::{
    day::{AocResult, Day, Type},
    load_input,
};

pub struct Day9;

#[derive(Clone, Debug)]
struct Point {
    c: i64,
    r: i64,
}

#[derive(Debug)]
struct Edge {
    from: Point,
    to: Point,
}

type Polygon = Vec<Edge>;

#[derive(Debug, Copy, Clone, PartialEq, Eq)]
enum Hit {
    Inside,
    Intersect,
    Outside,
}

impl Point {
    fn inside(&self, polygon: &Polygon) -> bool {
        let mut count = 0;
        for edge in polygon {
            match self.crosses(edge) {
                Hit::Intersect => count += 1,
                Hit::Inside => return true,
                _ => {}
            }
        }

        count % 2 == 1
    }

    fn crosses(&self, edge: &Edge) -> Hit {
        let lo_c = edge.from.c.min(edge.to.c);
        let hi_c = edge.from.c.max(edge.to.c);
        let lo_r = edge.from.r.min(edge.to.r);
        let hi_r = edge.from.r.max(edge.to.r);

        // if !(lo_c <= self.c && self.c <= hi_c) || !(lo_r <= self.r && self.r <= hi_r) {
        if !(lo_r <= self.r && self.r <= hi_r) {
            return Hit::Outside;
        }

        // divide by zero, horizontal edge
        if hi_r == lo_r {
            if self.r == hi_r {
                if lo_c <= self.c && self.c <= hi_c {
                    return Hit::Inside;
                } else if self.c < lo_c {
                    return Hit::Intersect;
                }
            }
            return Hit::Outside;
        }

        assert_eq!(lo_c, hi_c);
        if hi_c < self.c {
            return Hit::Outside;
        }

        // let h = (hi_r - lo_r) / (hi_c - lo_c);
        // let off = h * (self.c - lo_c);
        //
        if hi_c == self.c {
            return Hit::Inside;
        }

        Hit::Intersect
    }
}

impl Day for Day9 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);
        let mut part1 = 0i64;
        let mut part2 = 0;

        let points: Vec<(i64, i64)> = contents
            .lines()
            .map(|line| {
                let mut it = line.splitn(2, ',');
                let c: i64 = it.next().unwrap().parse().unwrap();
                let r: i64 = it.next().unwrap().parse().unwrap();
                (c, r)
            })
            .collect();

        for a in 0..points.len() {
            for b in a + 1..points.len() {
                let (ax, ay) = points[a];
                let (bx, by) = points[b];

                let grid = ((ay.abs_diff(by) + 1) * (ax.abs_diff(bx) + 1)) as i64;
                part1 = part1.max(grid);
            }
        }

        // part 2
        let points: Vec<Point> = contents
            .lines()
            .map(|line| {
                let mut it = line.splitn(2, ',');
                let c: i64 = it.next().unwrap().parse().unwrap();
                let r: i64 = it.next().unwrap().parse().unwrap();
                Point { c, r }
            })
            .collect();

        let mut p = Polygon::new();

        for i in 0..points.len() {
            let from = points[i].clone();
            let to = points[(i + 1) % points.len()].clone();
            p.push(Edge { from, to });
        }

        for ai in 0..points.len() {
            // println!("a: {ai}/{}", points.len());
            for bi in ai + 1..points.len() {
                let mut works = true;
                let a = points[ai].clone();
                let b = points[bi].clone();

                let min_r = a.r.min(b.r);
                let max_r = a.r.max(b.r);
                let min_c = a.c.min(b.c);
                let max_c = a.c.max(b.c);

                for r in min_r..=max_r {
                    if !works {
                        break;
                    }
                    let min_point = Point { r, c: min_c };
                    let max_point = Point { r, c: max_c };

                    if !min_point.inside(&p) || !max_point.inside(&p) {
                        works = false;
                        break;
                    }
                }
                for c in min_c..=max_c {
                    if !works {
                        break;
                    }
                    let min_point = Point { r: min_r, c };
                    let max_point = Point { r: max_r, c };

                    if !min_point.inside(&p) || !max_point.inside(&p) {
                        works = false;
                        break;
                    }
                }

                if works {
                    let grid = ((a.r.abs_diff(b.r) + 1) * (a.c.abs_diff(b.c) + 1)) as i64;
                    // println!("2: best={grid} = {:?} -> {:?}", a, b);
                    part2 = part2.max(grid);
                }
            }
        }

        Ok((part1, part2))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_crosses() {
        let point = Point { c: 10, r: 5 };

        let edge = Edge {
            from: Point { c: 11, r: 4 },
            to: Point { c: 11, r: 10 },
        };

        assert!(point.crosses(&edge) == Hit::Intersect);
    }

    #[test]
    fn test_all_crosses() {
        let contents = load_input!(Type::Sample);

        let points: Vec<Point> = contents
            .lines()
            .map(|line| {
                let mut it = line.splitn(2, ',');
                let c: i64 = it.next().unwrap().parse().unwrap();
                let r: i64 = it.next().unwrap().parse().unwrap();

                Point { c, r }
            })
            .collect();

        let edge = Edge {
            from: Point { c: 100, r: 0 },
            to: Point { c: 100, r: 100 },
        };
        for point in points {
            assert!(point.crosses(&edge) == Hit::Intersect);
        }
    }

    #[test]
    fn test_draw_map() {
        let contents = load_input!(Type::Sample);

        let points: Vec<Point> = contents
            .lines()
            .map(|line| {
                let mut it = line.splitn(2, ',');
                let c: i64 = it.next().unwrap().parse().unwrap();
                let r: i64 = it.next().unwrap().parse().unwrap();

                Point { c, r }
            })
            .collect();

        let max_r = 9;
        let max_c = 14;

        let mut grid: Vec<Vec<char>> = vec![vec!['.'; max_c]; max_r];

        let mut polygon = Polygon::new();
        for i in 0..points.len() {
            let from = points[i].clone();
            let to = points[(i + 1) % points.len()].clone();
            polygon.push(Edge { from, to });
        }

        for edge in &polygon {
            for _r in edge.from.r.min(edge.to.r)..=edge.from.r.max(edge.to.r) {
                for _c in edge.from.c.min(edge.to.c)..=edge.from.c.max(edge.to.c) {
                    grid[_r as usize][_c as usize] = 'X';
                }
            }
        }

        for point in points.clone() {
            let r: usize = point.r.try_into().unwrap();
            let c: usize = point.c.try_into().unwrap();
            grid[r][c] = '#';
        }

        for r in 0..max_r {
            for c in 0..max_c {
                let point = Point {
                    r: (r as i64),
                    c: (c as i64),
                };

                if point.inside(&polygon) {
                    grid[r][c] = 'O';
                }
            }
        }

        for r in 0..max_r {
            for c in 0..max_c {
                print!("{}", grid[r][c]);
            }
            println!();
        }
    }
}
