impl Solution {
    pub fn find_winners(matches: vec<vec<i32>>) -> vec<vec<i32>> {
        let copi = matches.clone();
        let all_players: hashset<_>= hashset::from_iter(copi.iter().flat_map(|e| e));
        let mut losers: hashmap<i32, i32> = hashmap::new();

        for m in matches {
            *losers.entry(m[1]).or_insert(0) += 1;
        }
        let mut not_losers: vec<i32> = vec![];
        let mut somewhat_losers: vec<i32> = vec![];

        for player in all_players {
            if !losers.contains_key(&player) {
                not_losers.push(*player);
            } else if let some(lost) = losers.get(&player) {
                if *lost == 1 {
                    somewhat_losers.push(*player);
                }
            }
        }
        not_losers.sort_unstable();
        somewhat_losers.sort_unstable();

        vec![not_losers, somewhat_losers]
    }
}
