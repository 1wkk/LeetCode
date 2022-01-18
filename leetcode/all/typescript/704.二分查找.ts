/*
 * @lc app=leetcode.cn id=704 lang=typescript
 *
 * [704] 二分查找
 */

// @lc code=start
function search(nums: number[], target: number): number {
  let l = 0,
    r = nums.length - 1
  while (l <= r) {
    const m = l + ~~((r - l) / 2)
    if (nums[m] > target) r = m - 1
    else if (nums[m] < target) l = m + 1
    else return m
  }
  return -1
}
// @lc code=end
