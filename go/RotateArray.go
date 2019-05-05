package main

func rotate(nums []int, k int) {
	l := len(nums)
	for i, a := 0, 0; a < l; i++ {
		c, p, done := i, nums[i], false
		for !done || c != i {
			done = true
			t := nums[(c+k)%l]
			nums[(c+k)%l] = p
			p, c = t, (c+k)%l
			a++
		}
	}
}
