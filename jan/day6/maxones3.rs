impl Solution {
    pub fn longest_ones(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0;
        let mut max = 0;
        let mut zeros = 0;

        for i in 0..nums.len() {
            if nums[i] == 0 {
                zeros += 1;
            }
            if zeros > k {
                if nums[left] == 0 {
                    zeros -= 1;
                }
                left += 1;
            }
            if zeros <= k {
                max = max.max(i - left + 1);
            }
        }
        max as i32
    }
}

