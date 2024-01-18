impl Solution {
    // i can't dp yet
    pub fn climb_stairs(n: i32) -> i32 {
        let mut a = 0;
        let mut b = 1;
        let mut num = 0;

        num = match n {
            1 => b,
            _ => {
                for _ in 1..=n {
                    num = a + b;
                    a = b;
                    b = num;
                }
                num
            }
        };
        num
    }
}
