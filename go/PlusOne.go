package main

func plusOne(digits []int) []int {
	carry := true
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 && carry {
			digits[i]++
			carry = false
		} else if carry {
			digits[i] = 0
			carry = true
			if i == 0 {
				return append([]int{1}, digits...)
			}
		}
	}
	return digits
}
