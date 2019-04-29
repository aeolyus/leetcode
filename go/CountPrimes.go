package main

func countPrimes(n int) int {
	sieve := make([]bool, n)
	for i := 2; i*i <= n; i++ {
		if sieve[i] == false {
			for j := i * i; j < n; j += i {
				sieve[j] = true
			}
		}
	}
	a := 0
	for i := 2; i < n; i++ {
		if sieve[i] == false {
			a++
		}
	}
	return a
}
