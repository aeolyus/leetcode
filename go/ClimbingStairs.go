package main

func climbStairs(n int) int {
  if n < 0 {
    return 0
  } else if n <= 2 {
    return n
  }
  a, b := 2, 1
  for i := 3; i <= n; i++ {
    a, b = a + b, a
  }
  return a
}
