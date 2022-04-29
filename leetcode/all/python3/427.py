"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recursion(x_start, y_start, x_end, y_end):
            n = x_end - x_start
            if n < 0:
                return None
            all_same = True
            v = grid[x_start][y_start]
            for x in range(x_start, x_end + 1):
                for y in range(y_start, y_end + 1):
                    if grid[x][y] != v:
                        all_same = False
                        break
            node = Node()
            if all_same:
                node.isLeaf = True
                node.val = v
            else:
                dis = n // 2
                node.isLeaf = False
                node.topLeft = recursion(x_start, y_start, x_start + dis, y_start + dis)
                node.topRight = recursion(
                    x_start, y_start + dis + 1, x_start + dis, y_end
                )
                node.bottomLeft = recursion(
                    x_start + dis + 1, y_start, x_end, y_start + dis
                )
                node.bottomRight = recursion(
                    x_start + dis + 1, y_start + dis + 1, x_end, y_end
                )
            return node

        n = len(grid)
        return recursion(0, 0, n - 1, n - 1)
