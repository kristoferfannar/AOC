use std::collections::{HashMap, HashSet};

use crate::{
    day::{AocResult, Day, Type},
    load_input,
};

pub struct Day8;

#[derive(Debug, Clone)]
struct Point3D {
    x: i64,
    y: i64,
    z: i64,
    bag: usize,
}

impl Point3D {
    fn dist(&self, other: &Point3D) -> i64 {
        let xd = self.x - other.x;
        let yd = self.y - other.y;
        let zd = self.z - other.z;
        return xd.pow(2) + yd.pow(2) + zd.pow(2);
    }
}

impl Day8 {
    fn part1(
        mut points: Vec<Point3D>,
        best: &Vec<(i64, (usize, usize))>,
        mut bags: HashMap<usize, Vec<usize>>,
        typ: &Type,
    ) -> i64 {
        let mut p1;
        let num_connections = match typ {
            Type::Sample => 10,
            Type::Actual => 1000,
        };

        for (_, (ai, bi)) in best[..num_connections].iter() {
            let a_id = points[*ai].bag;
            let b_id = points[*bi].bag;

            if a_id == b_id {
                continue;
            }

            let mut moved = bags.remove(&b_id).unwrap();

            for &ele in &moved {
                points[ele].bag = a_id;
            }

            bags.get_mut(&a_id).unwrap().append(&mut moved);
        }

        let mut count: Vec<(usize, i64)> = bags
            .iter()
            .map(|(&id, vec)| (id, vec.len() as i64))
            .collect();

        count.sort_by(|a, b| b.1.cmp(&a.1));

        p1 = 1;
        for (_bag_id, c) in &count[0..3] {
            p1 *= *c;
        }

        p1
    }

    fn part2(
        mut points: Vec<Point3D>,
        best: &Vec<(i64, (usize, usize))>,
        mut bags: HashMap<usize, Vec<usize>>,
    ) -> i64 {
        let mut non_empty_bags: HashSet<usize> = HashSet::new();

        for (&bag_id, _) in &bags {
            non_empty_bags.insert(bag_id);
        }

        for (_, (ai, bi)) in best.iter() {
            let a_id = points[*ai].bag;
            let b_id = points[*bi].bag;

            if a_id == b_id {
                continue;
            }
            let mut moved = bags.remove(&b_id).unwrap();

            for &ele in &moved {
                points[ele].bag = a_id;
            }
            bags.get_mut(&a_id).unwrap().append(&mut moved);

            non_empty_bags.remove(&b_id);
            if non_empty_bags.len() == 1 {
                return points[*ai].x * points[*bi].x;
            }
        }

        panic!();
    }
}

impl Day for Day8 {
    fn solve(typ: Type) -> AocResult<(i64, i64)> {
        let contents = load_input!(typ);
        let part1;
        let part2;

        let points: Vec<Point3D> = contents
            .trim_matches('\n')
            .split('\n')
            .enumerate()
            .map(|(i, line)| {
                let mut it = line.splitn(3, ',');

                let x = it.next().unwrap().parse().unwrap();
                let y = it.next().unwrap().parse().unwrap();
                let z = it.next().unwrap().parse().unwrap();

                Point3D { x, y, z, bag: i }
            })
            .collect();

        let mut best: Vec<(i64, (usize, usize))> = Vec::new();

        for ai in 0..points.len() {
            let a = &points[ai];
            for bi in ai + 1..points.len() {
                let b = &points[bi];

                // TODO make a heap?
                best.push((a.dist(b), (ai, bi)));
            }
        }

        best.sort_by(|a, b| a.0.cmp(&b.0));

        let mut bags: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..points.len() {
            let point = &points[i];
            bags.insert(point.bag, vec![point.bag]);
        }

        part1 = Day8::part1(points.clone(), &best, bags.clone(), &typ);
        part2 = Day8::part2(points.clone(), &best, bags.clone());

        Ok((part1, part2))
    }
}
