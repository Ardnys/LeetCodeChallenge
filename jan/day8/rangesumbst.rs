// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

impl TreeSolution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        // nice type
        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
        let mut sum: i32 = 0;

        queue.push_back(root);

        while let Some(elem) = queue.pop_front() {
            if let Some(node_rc) = elem {
                // borrow is for getting the reference to the contents of RefCell
                let node_ref = node_rc.borrow();

                let node_val = node_ref.val;
                if node_val >= low && node_val <= high {
                    sum += node_val;
                }

                // we have to clone them because of ownership rules
                if let Some(left) = node_ref.left.clone() {
                    queue.push_back(Some(left));
                }
                if let Some(right) = node_ref.right.clone() {
                    queue.push_back(Some(right));
                }
            }
        }
        sum
    }

}
