package main

type TreeNode struct {
  Val int
  Left *TreeNode
  Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
  if root == nil {
    return true
  }
  return same(root, root)
}

func same(a *TreeNode, b *TreeNode) bool {
  if a == nil && b == nil {
    return true
  } else if a == nil || b == nil {
    return false
  }
  return a.Val == b.Val && same(a.Left, b.Right) && same(a.Right, b.Left)
}
