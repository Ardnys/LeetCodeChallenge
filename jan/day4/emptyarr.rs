impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut le_map: HashMap<i32, i32> = HashMap::new();

        for num in nums {
            le_map.entry(num).and_modify(|e| {*e += 1}).or_insert(1);
        }
        let mut rem = 0;
        let mut ops  = 0;
        for (key, value) in le_map.iter() {
            rem = *value;
            while rem > 0 {
                (ops, rem) = match rem {
                    1 => (-1, 1),
                    2 => (ops + 1, 0),
                    3 => (ops + 1, 0),
                    4 => (ops + 2, 0),
                    _ => (ops + 1, rem - 3),
                };
                if ops == -1 {
                    return -1;
                }
            }
        }
        ops
    }
}
