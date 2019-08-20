func swap(i int, j int, nums []int) {
	temp := nums[i]
	nums[i] = nums[j]
	nums[j] = temp
}

func sortColors(nums []int) {
	start := 0
	end := len(nums) - 1
	for i := start; i <= end; i += 1 {
		if nums[i] == 0 {
			swap(start, i, nums)
			start += 1
		} else if nums[i] == 2 {
			swap(end, i, nums)
			end -= 1
			i -= 1
		}
	}
}
