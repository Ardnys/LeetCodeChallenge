impl Solution {
    // nice solution. would never think of it like this. study this.
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        // it should be at least max of the weights
        let mut left_cap = *weights.iter().max().unwrap();
        let mut right_cap: i32 = weights.iter().sum();

        while left_cap < right_cap {
            let cap = left_cap + (right_cap - left_cap) / 2;
            println!("cap: {cap}");
            if Self::ship_check_weight(&weights, &days, cap) {
                // something here
                println!("i guess it works: {cap}");
                right_cap = cap;
            } else {
                // something else here
                println!("naa: {cap}");
                left_cap = cap + 1;
            }
        }
        left_cap
    }
    pub fn ship_check_weight(weights: &Vec<i32>, days: &i32, capacity: i32) -> bool {
        let mut d = 1;
        let mut total_weight = 0;
        println!("trying capacity: {capacity}");

        for weight in weights {
            total_weight += weight;
            if total_weight > capacity {
                println!("too heavy: {total_weight}/{capacity}");
                total_weight = *weight;
                d += 1;
                if d > *days {
                    println!("too many days");
                    return false;
                }
            }
            println!("total: {total_weight} in {d}");
        }
        true
    }
}
