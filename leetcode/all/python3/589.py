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
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans

        # Iteration
        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            st.extend(reversed(node.children))

        # Recursion
        # def dfs(node):
        #     if node:
        #         ans.append(node.val)
        #         for c in node.children:
        #             dfs(c)
        # dfs(root)

        return ans
