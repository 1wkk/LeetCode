package main

import (
	"sort"
	"strconv"
)

func largestInteger(num int) int {
	s := strconv.Itoa(num)
	a := [2][]rune{}
	for _, v := range s {
		a[v&1] = append(a[v&1], v)
	}
	sort.Slice(a[0], func(i, j int) bool { return a[0][i] > a[0][j] })
	sort.Slice(a[1], func(i, j int) bool { return a[1][i] > a[1][j] })
	t := []rune{}
	for _, v := range s {
		k := int(v & 1)
		t = append(t, a[k][0])
		a[k] = append(a[k][:0], a[k][1:]...)
	}
	tt := string(t)
	ans, _ := strconv.Atoi(tt)
	return ans
}
