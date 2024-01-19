impl Solution {
    // i learned new stuff. hopefully
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let (mut left, mut right) = (1, piles.iter().copied().max().unwrap());

        while left < right {
            let mid = left + (right - left) / 2;
            if Self::can_eat(&piles, mid, h) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left as i32

    }
    fn can_eat(piles: &Vec<i32>, n: i32, h: i32) -> bool {
        piles.iter().fold(0f32, |acc, x| acc + (*x as f32/n as f32).ceil()) as i32 <= h
    }
    pub fn min_falling_path_sum(mut matrix: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (matrix.len() as i32, matrix[0].len() as i32);
        for i in 1..m {
            for j in 0..n {
                matrix[i as usize][j as usize] += matrix[(i - 1) as usize]
                    [(0.max(j - 1) as usize)..=((n - 1).min(j + 1) as usize)]
                    .iter()
                    .min()
                    .copied()
                    .unwrap();
            }
        }
        matrix[(m - 1) as usize].iter().copied().min().unwrap()
    }
}
