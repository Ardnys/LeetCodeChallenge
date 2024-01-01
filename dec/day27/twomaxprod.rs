fn main() {
    let nums = vec![2,3,5,7,2];
    let result = Solution::max_product(nums);
    println!("res: {}", result);

}
struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max1 = 0;
        let mut max2 = 0;

        for num in nums {
            if num > max1 {
                max2 = max1;
                max1 = num;
                // println!("new max {} and smoller max {}", max1, max2);
            } else if num == max1 || num > max2 {
                max2 = num;
                // println!("new smoller max {}", max2);
            } 
        }
        (max1-1) * (max2-1)

    }
}
