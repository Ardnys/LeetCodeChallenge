impl Solution {
    // nice solution
    pub fn eleganto_find_peak_element(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len()-1;

        while left < right {
            let mid = left + (right - left) / 2;
            if nums[mid] < nums[mid+1] {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        right as i32
    }

    // probs what i would have come up with
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut low = 1;
        let mut high = n-2;

        if n == 1 {
            return 0;
        } else if nums[0] > nums[1] {
            return 0;
        } else if nums[n-1] > nums[n-2] {
            return (n-1) as i32;
        }

        while low <= high {
            let mid = low + (high - low) / 2;
            
            if nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1] {
                return mid as i32;
            } else if nums[mid+1] > nums[mid] {
                low = mid + 1;
            } else if nums[mid] < nums[mid-1] {
                high = mid - 1;
            } 
        }
        0
    }
}
