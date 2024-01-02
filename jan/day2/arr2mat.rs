use std::collections::HashMap;

impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut occurence_map: HashMap<i32, usize> = HashMap::new();

        for num in nums {
            occurence_map.entry(num).and_modify(|e| {*e += 1}).or_insert(1);
        }

        let mat_size_rows = *occurence_map.values().max().unwrap_or(&1);
        let mat_size_cols = occurence_map.values().len();

        let mut matrix = vec![vec![0; mat_size_cols]; mat_size_rows];

        for (idx, key) in occurence_map.keys().enumerate() {
            if let Some(val) = occurence_map.get(key) {
                for i in 0..*val {
                    matrix[i][idx] = *key;
                }
            }
        }

        for row in matrix.iter_mut() {
            row.retain(|e| {*e != 0});
        }

        matrix
    }
}
