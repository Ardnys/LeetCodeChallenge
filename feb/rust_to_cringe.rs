impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: VecDeque<i32> = VecDeque::new();

        for token in tokens {
            match token.as_str() {
                "+" => {
                    let first = stack.pop_front().unwrap();
                    let second = stack.pop_front().unwrap();
                    stack.push_front(second + first);
                },
                "-" => {
                    let first = stack.pop_front().unwrap();
                    let second = stack.pop_front().unwrap();
                    stack.push_front(second - first);
                },
                "*" => {
                    let first = stack.pop_front().unwrap();
                    let second = stack.pop_front().unwrap();
                    stack.push_front(second * first);
                },
                "/" => {
                    let first = stack.pop_front().unwrap();
                    let second = stack.pop_front().unwrap();
                    stack.push_front(second / first);
                },
                _ => {
                    let res: i32 = token.parse().unwrap();
                    stack.push_front(res);
                }
            }
        }
        stack.pop_front().unwrap()
    }
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut cringe: HashMap<Vec<u32>, Vec<String>> = HashMap::new();

        for s in strs {
            let mut fm = vec![0; 26];
            for c in s.chars() {
                fm[(c as u8 - b'a') as usize] += 1;
            }
            cringe.entry(fm).or_insert(Vec::new()).push(s);
        }
        cringe.into_values().collect()
    }
}
