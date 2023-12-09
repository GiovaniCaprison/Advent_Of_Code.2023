use std::fs::File;
use std::error::Error;
use std::io::{BufRead, BufReader};
use regex::Regex;

fn main() -> Result<(), Box<dyn Error>> {

    let input = "/example/file/path.txt";

    part_1(input)?;
    part_2(input)?;

    Ok(())
}

fn part_1(path: &str) -> Result<usize, Box<dyn Error>> {
    let (seeds, maps) = parse_maps(path)?;

    let mut location  = usize::MAX;

    for mut key in seeds {

        for map in &maps {
            match map.lookup(key) {
                Ok(k)  |
                Err(k) => key = k,
            }
        }
        location = location.min(key);
    }
    println!("{}", location);
    Ok(0)
}

fn part_2(path: &str) -> Result<(), Box<dyn Error>> {
    let (seeds, maps) = parse_maps(path)?;

    let mut location  = usize::MAX;

    for range in seeds.chunks(2) {
        for mut key in range[0]..range[0] + range[1] {

            for map in &maps {
                match map.lookup(key) {
                    Ok(k)  |
                    Err(k) => key = k,
                }
            }
            location = location.min(key);
        }
    }
    println!("{}", location);
    Ok(())
}

#[derive(Debug)]
struct Map {
    _from   : String,
    _to     : String,
    entries : Vec<MapEntry>,
}
impl Map {
    fn lookup(&self, src: usize) -> Result<usize, usize> {
        let start = self.entries
            .binary_search_by_key(&src, |e| e.src_start)
            .map_or_else(|i| i.saturating_sub(1), |i| i);

        let entry = &self.entries[start];

        if src < entry.src_start ||
            src - entry.src_start >= entry.range_len {
            Err(src)
        } else {
            Ok(entry.dst_start + (src - entry.src_start))
        }
    }
}

#[derive(Debug)]
struct MapEntry {
    dst_start : usize,
    src_start : usize,
    range_len : usize,
}

enum ParserState {
    Seeds,
    MapTitle,
    MapEntries,
}

fn parse_maps(path: &str) -> Result<(Vec<usize>, Vec<Map>), Box<dyn Error>> {
    use ParserState::*;
    let file    = File::open(path)?;
    let reader  = BufReader::new(file);
    let nameexp = Regex::new(r"^(\w+)-to-(\w+)")?;
    let to_vec  = |s: &str| s.split_whitespace()
        .map(|s| s.parse())
        .collect::<Result<Vec<usize>,_>>();

    let mut state = Seeds;
    let mut seeds = Option::<Vec<usize>>::None;
    let mut map   = Option::<Map>::None;
    let mut maps  = Vec::new();

    for line in reader.lines().chain([Ok(String::new())]) {
        let line = line?;

        match state {
            Seeds => {
                if line.is_empty() {
                    state = MapTitle;
                } else {
                    let start = "seeds: ".len();
                    seeds = Some(to_vec(&line.as_str()[start..])?);
                }
            },
            MapTitle => {
                let caps = nameexp.captures(line.as_str()).ok_or("No match")?;
                let from = caps[1].to_string();
                let to   = caps[2].to_string();

                map = Some(Map { _from: from, _to: to, entries: Vec::new() });

                state = MapEntries;
            },
            MapEntries => {
                if line.is_empty() {
                    if let Some(mut map) = map.take() {
                        map.entries.sort_unstable_by_key(|e| e.src_start);
                        maps.push(map);
                    }
                    state = MapTitle;
                } else {
                    let data = to_vec(line.as_str())?;

                    map.as_mut().ok_or("No map!")?.entries.push(
                        MapEntry {
                            dst_start : data[0],
                            src_start : data[1],
                            range_len : data[2],
                        }
                    );
                }
            },
        }
    }
    Ok((seeds.unwrap(), maps))
}
