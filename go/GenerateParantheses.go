package main

func generateParenthesis(n int) []string {
	res := make([]string, 0)
	helpParan(n, n, "", &res)
	return res
}

func helpParan(o int, c int, curr string, res *[]string) {
	if o == 0 && c == 0 {
		*res = append(*res, curr)
		return
	}
	if o > 0 {
		helpParan(o-1, c, curr+"(", res)
	}
	if c > o && c > 0 {
		helpParan(o, c-1, curr+")", res)
	}
}
