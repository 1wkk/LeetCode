package main

import "math"

func largestPalindrome(n int) int {
	if n == 1 {
		return 9
	}
	// up is the limit of the left p
	up := int(math.Pow10(n) - 1)
	for left := up; left >= int(math.Pow10(n-1)); left-- {
		p := left
		for x := left; x > 0; x /= 10 {
			p = p*10 + x%10
		}
		// p is result of a * b, here a is x
		for x := up; x*x >= p; x-- {
			if p%x == 0 {
				return p % 1337
			}
		}
	}
	return -1
}
