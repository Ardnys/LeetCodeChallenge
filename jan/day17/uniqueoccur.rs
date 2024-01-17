impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut occurence_map: HashMap<i32, u32> = HashMap::new();
        let mut occurence_set: HashSet<u32> = HashSet::new();

        for e in arr {
            *occurence_map.entry(e).or_insert(0) += 1;
        }

        for val in occurence_map.values() {
            if let None = occurence_set.get(val) {
                occurence_set.insert(*val);
            }
            return false;
        }
        true
    }
}
