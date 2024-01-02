impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut nums: HashSet<i32> = HashSet::new();
        nums.insert(n);

        Self::is_unhappy(n, nums)
    }
    pub fn is_unhappy(n: i32, mut nums: HashSet<i32>) -> bool {
        if n == 1 {
            return true;
        }
        let mut num = n;
        let mut sq_sum = 0;
        while num > 0 {
            let rem = num % 10;
            sq_sum += rem * rem;
            num /= 10;
        }
        if nums.contains(&sq_sum) {
            return false;
        }
        nums.insert(sq_sum);

        Self::is_unhappy(sq_sum, nums)
    }
}

