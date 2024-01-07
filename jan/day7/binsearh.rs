impl Solution {
    unsafe fn guess_number(n: i32) -> i32 {
        let mut right = n;
        let mut left = 1;

        loop {
            let num = left + (right - left) / 2;
            match guess(num) {
                -1 => right = num - 1,
                1 => left = num + 1,
                _ => return num,
            }
        }    
    }
}

