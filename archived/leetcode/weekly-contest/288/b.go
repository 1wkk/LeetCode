package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func minimizeResult(expression string) (ans string) {
	ss := strings.Split(expression, "+")
	l, r := ss[0], ss[1]
	for i, min := 0, math.MaxInt32; i < len(l); i++ {
		a := 1
		if i > 0 {
			a, _ = strconv.Atoi(l[:i])
		}
		b, _ := strconv.Atoi(l[i:])
		for j := 1; j <= len(r); j++ {
			c, _ := strconv.Atoi(r[:j])
			d := 1
			if j < len(r) {
				d, _ = strconv.Atoi(r[j:])
			}
			calc := a * (b + c) * d
			if calc < min {
				min = calc
				ans = fmt.Sprintf("%s(%s+%s)%s", l[:i], l[i:], r[:j], r[j:])
			}

		}
	}
	return
}
