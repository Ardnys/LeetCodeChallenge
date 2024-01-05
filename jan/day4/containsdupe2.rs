impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        // check if the elements exist in the map
        // if they exist, subtract the index and check if it's in the windows size
        let mut le_map: HashMap<i32, usize> = HashMap::new();
        let k = k as usize;

        for (i, num) in nums.iter().enumerate() {
            if let Some(idx) = le_map.get(num) {
                let window = idx.abs_diff(i);
                if window <= k {
                    return true;
                    println!("nice window {window}");
                } else {
                    println!("not nice window {window}");
                }
            } else {
                le_map.insert(*num, i);
            }
        }
        false
    }
}
