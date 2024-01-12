impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let n = s.len();
        let vowels = HashSet::from(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
        if let (Some(first), Some(last)) = (s.get(0..n/2), s.get(n/2..n)) {
            // println!("first: {first}, last: {last}");
            let vow_count = first.chars().filter(|&c| vowels.contains(&c)).count();
            let uh = last.chars().filter(|&c| vowels.contains(&c)).count();
            return uh == vow_count;
        }
        false
    }
}
