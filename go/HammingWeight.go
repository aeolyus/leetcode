package main

func hammingWeight(num uint32) int {
  i := 0
  for num > 0 {
    i++
    num &= num - 1
  }
  return i
}
