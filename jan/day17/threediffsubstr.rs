impl Solution {
    pub fn count_good_substrings(s: String) -> i32 {
        let mut good_substr = 0;
        let n = s.len();

        for i in 2..n {
            let set: HashSet<_> = s.get(i-2..=i).unwrap().chars().collect();

            if set.len() == 3 {
                good_substr += 1;
            }
        }
        good_substr as i32
    }
}
