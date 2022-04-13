package main

import "math"

func Sum (nums []int) int{
	sum := 0
	for _, num := range nums{
		sum += num
	}
	return sum
}

func maximumWealth(accounts [][]int) int {
	max := 0
	for _, account := range accounts{
		max = int(math.Max(float64(max), float64(Sum(account))))
	}
	return max
}