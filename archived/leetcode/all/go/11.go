package main

// @tag - two pointers
func maxArea(h []int) int {
	l, r, ans := 0, len(h)-1, 0
	for l < r {
		ans = Max(ans, Min(h[l], h[r])*(r-l))
		if h[l] < h[r] {
			l++
		} else {
			r--
		}
	}
	return ans
}

func Max(a, b int) int {
	if a < b {
		return b
	} else {
		return a
	}
}

func Min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
