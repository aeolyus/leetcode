package main

func permute(nums []int) [][]int {
	r := make([][]int, 0)
	helpP(nums, make([]int, 0), &r)
	return r
}

func helpP(n []int, c []int, res *[][]int) {
	if len(n) == 0 {
		*res = append(*res, c)
		return
	}
	for i := 0; i < len(n); i++ {
		N := make([]int, len(n)-1)
		copy(N, n[:i])
		copy(N[i:], n[i+1:])
		C := make([]int, len(c))
		copy(C, c)
		helpP(N, append(C, n[i]), res)
	}
}
