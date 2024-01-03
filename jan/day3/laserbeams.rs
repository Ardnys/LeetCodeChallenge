impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut beams = 0i32;
        let mut previous = 0i32;
        let mut ones = 0i32;
        for lasers in bank {
            ones = lasers.chars().filter(|&c| c == '1').count() as i32;
            if ones > 0  && previous > 0 {
                beams += ones * previous;
                previous = ones;
            } else if ones > 0 {
                previous = ones;
            }
        }
        beams
    }
}
