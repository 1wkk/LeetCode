/*
 * @lc app=leetcode.cn id=1 lang=typescript
 *
 * [1] 两数之和
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
  const map = new Map()
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i],
      l = target - num
    if (map.has(l)) return [map.get(l), i]
    map.set(num, i)
  }
  return []
}
// @lc code=end
