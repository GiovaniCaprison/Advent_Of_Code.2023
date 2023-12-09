use std::{
    env,
    io::{self, Read},
    process::exit,
};

struct TimeDistance {
    time: u32,
    distance: u32,
}

fn parse_input(input: &str) -> Vec<TimeDistance> {
    input
        .split("\n")
        .filter(|x| !x.is_empty())
        .collect::<Vec<&str>>()
        .chunks(2)
        .map(|chunk| TimeDistance {
            time: chunk[0]
                .split_whitespace()
                .nth(1)
                .and_then(|s| s.parse().ok())
                .expect("Invalid time format"),
            distance: chunk[1]
                .split_whitespace()
                .nth(1)
                .and_then(|s| s.parse().ok())
                .expect("Invalid distance format"),
        })
        .collect()
}

fn calculate_winning_ways(time_distance_pairs: &[TimeDistance], rate: u32) -> u32 {
    time_distance_pairs.iter().fold(1, |prod, pair| {
        prod * (0..=pair.time)
            .filter(|&time| time * rate * (pair.time - time) > pair.distance)
            .count() as u32
    })
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() <= 1 {
        eprintln!("First argument must be the part number");
        exit(1);
    }

    let part = args[1]
        .parse::<u32>()
        .expect("Part number must be a valid number");

    let mut input = String::new();
    io::stdin()
        .read_to_string(&mut input)
        .expect("Failed to read from stdin");

    let time_distance_pairs = parse_input(&input);

    match part {
        1 | 2 => {
            let output = calculate_winning_ways(&time_distance_pairs, 1);
            println!("{output}");
        }
        _ => eprintln!("Part number must be 1 or 2"),
    }
}
