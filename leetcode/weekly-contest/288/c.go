package main

import (
	"container/heap"
)

type hp []int

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i] < h[j] }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *hp) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *hp) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maximumProduct(nums []int, k int) int {
	h := hp(nums)
	for heap.Init(&h); k > 0; k-- {
		h[0]++
		heap.Fix(&h, 0)
	}
	ans := 1
	for _, num := range nums {
		ans = ans * num % (1e9 + 7)
	}
	return ans
}
