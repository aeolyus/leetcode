package main

func findDisappearedNumbers(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		for nums[i]-1 != i && nums[i] != nums[nums[i]-1] {
			nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
		}
	}
	result := []int{}
	for i := 0; i < len(nums); i++ {
		if nums[i]-1 != i {
			result = append(result, i+1)
		}
	}
	return result
}
