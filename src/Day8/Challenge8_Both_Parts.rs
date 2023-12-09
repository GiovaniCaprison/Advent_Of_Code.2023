use std::fs;

fn main() {
    let content = fs::read_to_string("input.txt")
        .expect("Something went wrong reading the file");

    let sequences: Vec<Vec<i64>> = content
        .lines()
        .map(|l| {
            l.split_whitespace()
                .map(|x| x.parse::<i64>().expect("Parse error"))
                .collect()
        })
        .collect();

    let mut part1_answer: i64 = 0;
    let mut part2_answer: i64 = 0;

    sequences.iter().for_each(|s| {
        part1_answer += extrapolate_value_part1(s);
        part2_answer += extrapolate_value_part2(s);
    });

    println!("Part 1 Answer: {}", part1_answer);
    println!("Part 2 Answer: {}", part2_answer);
}

fn extrapolate_value_part2(x: &Vec<i64>) -> i64 {
    if is_all_zeroes(x) {
        return 0;
    }

    let value_to_prepend = extrapolate_value_part2(&generate_differences(x));

    x.first().unwrap() - value_to_prepend
}

fn extrapolate_value_part1(x: &Vec<i64>) -> i64 {
    if is_all_zeroes(x) {
        return 0;
    }

    let value_to_append = extrapolate_value_part1(&generate_differences(x));

    x.last().unwrap() + value_to_append
}

fn generate_differences(x: &Vec<i64>) -> Vec<i64> {
    x.windows(2).map(|x| {
        x[1] - x[0]
    }).collect()
}

fn is_all_zeroes(x: &Vec<i64>) -> bool {
    x.iter().all(|n| *n == 0)
}
