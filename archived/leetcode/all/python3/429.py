"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[int]:
        ans = []

        if not root:
            return ans

        q = deque()
        q.append(root)

        while q:
            n = len(q)
            res = []
            for _ in range(n):
                node = q.popleft()
                res.append(node.val)
                q.extend(node.children)
            ans.append(res)

        return ans
