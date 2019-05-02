class ConvertBSTtoGreaterTree {
	int i = 0;
	public TreeNode convertBST(TreeNode root) {
		if (root == null) {
			return null;
		}
		convertBST(root.right);
		i += root.val;
		root.val = i;
		convertBST(root.left);
		return root;
	}

	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
}
