/*
 * @lc app=leetcode.cn id=219 lang=typescript
 *
 * [219] 存在重复元素 II
 */

// @lc code=start
function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const set = new Set<number>()
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    if (i > k) set.delete(nums[i - k - 1])
    if (set.has(num)) return true
    set.add(num)
  }
  return false
}
// @lc code=end
