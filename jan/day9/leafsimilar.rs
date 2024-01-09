impl TreeSolution {
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn inorder(node: Option<Rc<RefCell<TreeNode>>>, list: &mut Vec<i32> ) {
            if let Some(node_rc) = node {
                let node_ref = node_rc.borrow();

                if let Some(left) = node_ref.left.clone() {
                    inorder(Some(left), list);
                }

                if let (None, None) = (node_ref.left.clone(), node_ref.right.clone()) {
                    let node_val = node_ref.val;
                    list.push(node_val);
                }

                if let Some(right) = node_ref.right.clone() {
                    inorder(Some(right), list);
                }

            }
         }

        let mut v1: Vec<i32> = Vec::new();
        let mut v2: Vec<i32> = Vec::new();

        inorder(root1, &mut v1);
        inorder(root2, &mut v2);

        v1 == v2
    }
}
