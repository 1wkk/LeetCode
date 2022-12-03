package main

type Node struct {
	Val      int
	Children []*Node
}

func levelOrder(root *Node) [][]int {
	ans := [][]int{}
	if root == nil {
		return ans
	}
	q := []*Node{root}
	for len(q) > 0 {
		_len := len(q)
		_ans := []int{}
		for _, node := range q[:] {
			_ans = append(_ans, node.Val)
			q = append(q, node.Children...)
		}
		q = q[_len:]
		ans = append(ans, _ans)
	}
	return ans
}
