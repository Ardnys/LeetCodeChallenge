impl Solution {
    // sort the potions, order does not matter anyway.
    // ceil(success/spells[i]) for the min multiplier.
    // search the min multiplier in the potions. say, its xth index
    // then we have potions.len() - x successful pairs

    /* TWO RUST APPROACHES
    *  First, the pleb one. That's how I think.
    *  Then, second, the _iditomatic_ Rust solution. Though it's just mapping it, it's a bit
    *  faster.
    */
    pub fn pleb_successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let n = potions.len() as i32;

        let mut potions = potions.clone();
        potions.sort_unstable();

        let mut succ_pairs: Vec<i32> = Vec::new();

        for spell in spells {
            // ardnys sekai anime reference
            // also convert to float to ceil it
            let minumi = (success as f64/spell as f64).ceil() as i32;
            // partition_point is like binary search but works for ranges.
            // idk if its slower but it seemed cool thus i am using it.
            let idx = potions.partition_point(|&x| x < minumi) as i32;
            let pairs: i32 = n - idx;

            succ_pairs.push(pairs);
        }
        succ_pairs

    }

    pub fn idiomatic_successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let n = potions.len() as i32;

        let mut potions = potions.clone();
        potions.sort_unstable();

        let succ_pairs: Vec<i32> = spells
            .into_iter()
            .map(|spell| {
                let minumi = (success as f64/spell as f64).ceil() as i32;
                let idx = potions.partition_point(|&x| x < minumi) as i32;
                let pairs = n - idx;
                pairs as i32
            })
            .collect();

        succ_pairs
    }
}
