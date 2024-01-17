impl Solution {
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
        let n  = code.len();
        let mut res: Vec<i32> = vec![0; n];
        if k < 0 {
            for i in 0..n {
                let mut sum: i32 = 0;
                // i love me some algebraic types and safety
                // just lost my mind trying to walk around that thing
                // that's all
                for j  in 1..(k*-1)+1 {
                    let mut r:i32 = i as i32-j as i32;
                    if  r < 0  { r=r+n as i32; }
                    sum += code[r as usize];
                }
                res[i] = sum;
            }

        } else if k > 0 {
            for i in 0..n {
                let mut sum: i32 = 0;
                for j in i+1..=(i+k as usize) {
                    sum += code[j%n];
                }
                res[i] = sum;
            }
        } else {
            return res;
        }
        res
    }
}
