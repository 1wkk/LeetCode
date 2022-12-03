"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        if not root:
            return ans

        st = [root]
        while st:
            node = st.pop()
            ans.append(node.val)
            for c in node.children:
                st.append(c)

        # def dfs(node):
        #     if node:
        #         for c in node.children:
        #             dfs(c)
        #         ans.append(node.val)

        # dfs(root)
        return ans[::-1]
