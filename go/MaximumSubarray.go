package main

func maxSubArray(nums []int) int {
  max := nums[0]
  curr := nums[0]
  for _, i := range nums[1:] {
    if curr < 0 {
      curr = 0;
    }
    curr += i
    if max < curr {
      max = curr
    }
  }
  return max
}
