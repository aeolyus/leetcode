package main

func rob(nums []int) int {
	curr, prev := 0, 0
	for i := 0; i < len(nums); i++ {
		t := curr
		if prev+nums[i] > curr {
			curr = prev + nums[i]
		}
		prev = t
	}
	return curr
}
