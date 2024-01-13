impl Solution {
    pub fn min_steps_arr(s: String, t: String) -> i32 {
        let mut freq_s = vec![0; 26];
        let mut freq_t = vec![0; 26];

        for c in s.chars() {
            // that's a better way to index freq array
            freq_s[(c as u8 - b'a') as usize] += 1;
        }
        for c in t.chars() {
            freq_t[(c as u8 - b'a') as usize] += 1;
        }

        let mut count = 0;

        for i in 0..26 {
            // this is like counting the other way from my original solution
            if freq_t[i] < freq_s[i] {
                count += freq_s[i] - freq_t[i];
            }
        }
        count as i32
    }

    pub fn min_steps(s: String, t: String) -> i32 {
        let mut s_map = HashMap::new();

        for c in s.chars() {
            *s_map.entry(c).or_insert(0) += 1;
        }
        
        let mut count = 0;

        // direct entry lookup is faster. thanks gippity
        for c in t.chars() {
            match s_map.entry(c) {
                std::collections::hash_map::Entry::Occupied(mut entry) => {
                    if *entry.get() > 0 {
                        *entry.get_mut() -= 1;
                    } else {
                        count += 1;
                    }
                },
                std::collections::hash_map::Entry::Vacant(_) => {
                    count += 1;
                },
            }
        }

        // my pleb solution
        // for c in t.chars() {
        //     if let Some(val) = s_map.get(&c) {
        //         // update the value
        //         if *val > 0 {
        //             *val -= 1;
        //         } else {
        //             count += 1;
        //         }
        //
        //     } else {
        //         count += 1;
        //     }
        // }
        count as i32
    }
}
