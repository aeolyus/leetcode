package main

func trailingZeroes(n int) int {
	c := 0
	for n >= 5 {
		n /= 5
		c += n
	}
	return c
}
