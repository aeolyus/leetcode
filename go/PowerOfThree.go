package main

func isPowerOfThree(n int) bool {
  i := float64(n)
  for i > 1 {
    i /= 3.0
  }
  if i == 1 {
    return true
  }
  return false
}
