package main

func isValid(s string) bool {
	stk := make([]rune, 0)
	for _, c := range s {
		if c == '(' || c == '{' || c == '[' {
			stk = append(stk, c)
		} else if len(stk) > 0 && match(stk[len(stk)-1], c) {
			stk = stk[:len(stk)-1]
		} else {
			return false
		}
	}
	if len(stk) == 0 {
		return true
	}
	return false
}

func match(a, b rune) bool {
	return (a == '(' && b == ')') || (a == '[' && b == ']') || (a == '{' && b == '}')
}
