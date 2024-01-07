impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut zero_idx = 0;
        let mut max = 0;
        let mut is_deleted = false;

        for i in 0..nums.len() {
            if nums[i] == 0 {
                if is_deleted {
                    // something
                    max = max.max(i-left-1);
                    println!("new max: {max}");
                    left = zero_idx + 1;
                    zero_idx = i;
                } else {
                    println!("first zero at: {i}");
                    zero_idx = i;
                    is_deleted = true;
                }
            } else {
                max = max.max(i-left);
            }
        }
        max as i32
    }
}
