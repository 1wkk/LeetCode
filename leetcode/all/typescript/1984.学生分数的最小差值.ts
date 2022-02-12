/*
 * @lc app=leetcode.cn id=1984 lang=typescript
 *
 * [1984] 学生分数的最小差值
 */

// @lc code=start
function minimumDifference(nums: number[], k: number): number {
    // fuck => js array sort by string by default
    nums.sort((a, b) => a - b)
    let ans = Infinity
    for (let i = 0; i < nums.length - k + 1; i++)
        ans = Math.min(ans, nums[i + k - 1] - nums[i])
    return ans
}
// @lc code=end
