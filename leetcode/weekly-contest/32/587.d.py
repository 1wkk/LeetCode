from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p, q, r):
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        trees.sort()
        hull = [0]
        used = [False for _ in range(n)]
        for i in range(1, n):
            while (
                len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) > 0
            ):
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while (
                    len(hull) > m
                    and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) > 0
                ):
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        hull.pop()
        return [trees[i] for i in hull]
