impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        // incredible bubble sort
        for i in 0..nums.len() {
            for j in 0..nums.len() {
                if nums[i] < nums[j] {
                    nums.swap(i, j);
                }
            }
        }
    }
}
