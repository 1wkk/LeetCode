from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_left, max_left = {}, {}
        min_stack, max_stack = [], []
        for i, num in enumerate(nums):
            while min_stack and nums[min_stack[-1]] > num:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            # 找到逻辑大的数 所以相等，但是下标小的数，逻辑小，排除
            while max_stack and nums[max_stack[-1]] <= num:
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)

        min_right, max_right = {}, {}
        min_stack, max_stack = [], []
        for i, num in enumerate(nums[::-1]):
            while min_stack and nums[min_stack[-1]] >= num:
                min_stack.pop()
            min_right[n - 1 - i] = min_stack[-1] if min_stack else n
            min_stack.append(n - 1 - i)

            while max_stack and nums[max_stack[-1]] < num:
                max_stack.pop()
            max_right[n - 1 - i] = max_stack[-1] if max_stack else n
            max_stack.append(n - 1 - i)

        min_sum, max_sum = 0, 0
        for i, num in enumerate(nums):
            # 以 num 为最大（小）值的子数组的个数 * num
            min_sum += (min_right[i] - i) * (i - min_left[i]) * num
            max_sum += (max_right[i] - i) * (i - max_left[i]) * num
        return max_sum - min_sum
