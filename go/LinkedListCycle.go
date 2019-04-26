package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	a := head
	if a == nil || a.Next == nil {
		return false
	}
	b := head.Next.Next
	for a != b && b != nil {
		a = a.Next
		if b.Next == nil || b.Next.Next == nil {
			return false
		}
		b = b.Next.Next
	}
	if b == nil {
		return false
	}
	return true
}
