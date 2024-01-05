impl Solution {
    pub fn maximum_strong_pair_xor(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut max_xor = 0;
        for i in 0..n {
            for j in 0..n {
                let elem1 = nums[i];
                let elem2 = nums[j];
                if elem1.abs_diff(elem2) <= elem1.min(elem2).try_into().unwrap() {
                    max_xor = max_xor.max(elem1 ^ elem2);
                }
            }
        }
        max_xor
    }
}
