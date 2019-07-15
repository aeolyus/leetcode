package main

func maxArea(height []int) int {
	max, width := 0, len(height)-1
	a, b := 0, width
	for a != b {
		height, h1, h2 := 0, height[a], height[b]
		if h1 < h2 {
			a++
			height = h1
		} else {
			b--
			height = h2
		}
		area := height * width
		if area > max {
			max = area
		}
		width--
	}
	return max
}
