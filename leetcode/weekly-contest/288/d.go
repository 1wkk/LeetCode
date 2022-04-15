package main

import (
	"sort"
)

func maximumBeauty(flowers []int, nf int64, target int, full int, partial int) int64 {
	n := len(flowers)
	for i, v := range flowers {
		flowers[i] = Min(v, target)
	}
	sort.Slice(flowers, func(i, j int) bool { return flowers[i] > flowers[j] })
	sum := Sum(flowers)
	ans := 0
	if int64(target*n-sum) <= nf {
		ans = full * n
	}
	pre := 0
	r := 0
	for i, v := range flowers {
		if i != 0 {
			pre += flowers[i-1]
		}
		if v == target {
			continue
		}
		rest := nf - int64(target*i-pre)
		if rest < 0 {
			break
		}
		for !(r >= i && (flowers[r]*(n-r))-sum <= int(rest)) {
			sum -= flowers[r]
			r++
		}
		rest -= int64(flowers[r]*(n-r) - sum)
		ans = Max(ans, full*i+partial*Min(target-1, flowers[r]+int(rest/int64(n-r))))
	}
	return int64(ans)
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

func Sum(a []int) int {
	sum := 0
	for _, v := range a {
		sum += v
	}
	return sum
}
