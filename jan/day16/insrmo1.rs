use std::collections::HashMap;
use rand::prelude::*;

struct RandomizedSet {
    rand_map: HashMap<i32, usize>,
    heap: Vec<i32>,
}
/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        RandomizedSet {
            rand_map: HashMap::new(),
            heap: Vec::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if !self.rand_map.contains_key(&val) {
            self.rand_map.insert(val, self.heap.len());
            self.heap.push(val);
            return true;
        }
        false
    }

    fn remove(&mut self, val: i32) -> bool {
        if let Some(idx) = self.rand_map.remove(&val) {
            if let Some(&val2) = self.heap.last() {
                self.heap.swap_remove(idx);
                if val != val2 {
                    *self.rand_map.get_mut(&val2).unwrap() = idx;
                }
            }
            return true;
        }
        false
    }

    fn get_random(&self) -> i32 {
        *self.heap.choose(&mut rand::thread_rng()).unwrap()
    }

}
