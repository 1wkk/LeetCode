from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}

        for x in nums2[::-1]:
            while stack and stack[-1] <= x:
                stack.pop()
            dic[x] = stack[-1] if stack else -1
            stack.append(x)

        return [dic[x] for x in nums1]
