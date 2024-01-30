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
}
