package main

import "strconv"

func countAndSay(n int) string {
	res := "1"
	n--
	for ; n > 0; n-- {
		res = help(res)
	}
	return res
}

func help(s string) string {
	r := ""
	for i, j := 0, 0; i < len(s); {
		for j = 0; j+i < len(s) && s[i] == s[i+j]; j++ {
		}
		r += strconv.Itoa(j) + s[i:i+1]
		i += j
	}
	return r
}
