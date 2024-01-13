// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        // trivial linked list question stirs up the noodle in Rust
        let mut head = head;
        let mut current = &mut head;
        loop {
            match current {
                None => break,
                Some(node) if node.val == val => {
                    *current = node.next.take();
                },
                Some(node) => {
                    current = &mut node.next;
                },
            }
        }
        head
    }

}
