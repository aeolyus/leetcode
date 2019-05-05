package main

import "strings"

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	i, j := 0, len(s)-1
	for i < j {
		for !isAlphaNum(s[i]) && i < j {
			i++
		}
		for !isAlphaNum(s[j]) && i < j {
			j--
		}
		if isAlphaNum(s[i]) && isAlphaNum(s[j]) && s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func isAlphaNum(c byte) bool {
	return '0' <= c && c <= '9' || 'a' <= c && c <= 'z'
}
