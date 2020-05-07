package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invert(node *TreeNode) {
	if node != nil {
		invert(node.Left)
		invert(node.Right)
		node.Left, node.Right = node.Right, node.Left
	}
}

func invertTree(root *TreeNode) *TreeNode {
	invert(root)
	return root
}
