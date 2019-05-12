package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	res := make([]int, 0)
	c := root
	for c != nil {
		if c.Left == nil {
			res = append(res, c.Val)
			c = c.Right
		} else {
			p := c.Left
			for p.Right != nil && p.Right != c {
				p = p.Right
			}
			if p.Right == nil {
				p.Right = c
				t := c
				c, t.Left = c.Left, nil
			}
		}
	}
	return res
}
