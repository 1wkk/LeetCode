/*
 * @lc app=leetcode.cn id=334 lang=typescript
 *
 * [334] 递增的三元子序列
 */

// @lc code=start
function increasingTriplet(nums: number[]): boolean {
  const inc = new Array(3).fill(Infinity)
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    if (inc[2] < num) return true
    else if (inc[1] < num && num < inc[2]) inc[2] = num
    else if (num < inc[1]) inc[1] = num
  }
  return false
}
// @lc code=end
