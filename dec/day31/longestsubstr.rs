use std::collections::HashMap;

fn main() {
    let s = String::from("abca");
    let len = Solution::max_length_between_equal_characters(s);
    println!("len: {len}");

}

struct Solution;

impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let mut substr_map: HashMap<char, i32> = HashMap::new();
        let mut mx = -1;

        for (i, chr) in s.char_indices() {
            if !substr_map.contains_key(&chr) {
                println!("{i} -> {chr}");
                substr_map.insert(chr, i as i32);
            } else {
                if let Some(idx) = substr_map.get(&chr) {
                    if i as i32 - idx > mx {
                        mx = i as i32 - idx -1;
                        println!("new max: {mx} for char: {chr}");
                    }
                }

            }
        }
       mx as i32
    }
}
