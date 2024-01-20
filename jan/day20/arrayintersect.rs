use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    // std library
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let set1: HashSet<_> = HashSet::from_iter(nums1);
        let set2: HashSet<_> = HashSet::from_iter(nums2);
        let res: Vec<_> = set1.intersection(&set2).copied().collect();
        res
    }
    // faster way
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut res: HashSet<i32> = HashSet::new();
        let set1: HashSet<_> = HashSet::from_iter(nums1);

        for num in nums2 {
            if set1.contains(&num) {
                res.insert(num);
            }
        }
        Vec::from_iter(res)
    }

}
