/*
 * @lc app=leetcode.cn id=747 lang=typescript
 *
 * [747] 至少是其他数字两倍的最大数
 */

// @lc code=start
function dominantIndex(nums: number[]): number {
  if (nums.length < 2) return 0
  let a = -1,
    b = 0
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > nums[b]) {
      a = b
      b = i
    } else if (a === -1 || nums[i] > nums[a]) a = i
  }
  return nums[b] >= 2 * nums[a] ? b : -1
}
// @lc code=end
