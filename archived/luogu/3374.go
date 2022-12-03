package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	in  = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	f   = [2000000]int{}
	a   []int
)

func build(k, l, r int) {
	if l == r {
		f[k] = a[l]
		return
	}
	m := (l + r) >> 1
	build(2 * k, l, m)
	build(2 * k + 1, m + 1, r)
	f[k] = f[2 * k] + f[2 * k + 1]
}

func add(k, l, r, x, y int) {
	f[k] += y
	if l == r {
		return
	}
	m := (l + r) >> 1
	if x <= m {
		add(2 * k, l, m, x, y)
	} else {
		add(2 * k + 1, m + 1, r, x, y)
	}
}

func _sum(k, l, r, x, y int) int {
	if l == x && r == y {
		return f[k]
	}
	m := (l + r) >> 1
	if y <= m {
		return _sum(2 * k, l, m, x, y)
	} else {
		if x > m {
			return _sum(2 * k + 1, m + 1, r, x, y)
		} else {
			return _sum(2 * k, l, m, x, m) + _sum(2 * k + 1, m + 1, r, m + 1, y)
		}
	}
}

func main() {
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	a = make([]int, n + 1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &a[i])
	}
	build(1, 1, n)
	var op, x, y int
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &op, &x, &y)
		switch op {
		case 1:
			add(1, 1, n, x, y)
		case 2:
			fmt.Fprintln(out, _sum(1, 1, n, x, y))
		}
	}
}
