package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	stack := make([]int, 0)
	ptr := head
	for ptr != nil {
		stack = append(stack, ptr.Val)
		ptr = ptr.Next
	}
	for head != nil {
		if head.Val == stack[len(stack)-1] {
			stack = stack[:len(stack)-1]
		}
		head = head.Next
	}
	return len(stack) == 0
}
