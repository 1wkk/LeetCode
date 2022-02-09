/*
 * @lc app=leetcode.cn id=2006 lang=typescript
 *
 * [2006] 差的绝对值为 K 的数对数目
 */

// @lc code=start
function countKDifference(nums: number[], k: number): number {
    let ans = 0
    const map = {}
    for (const num of nums) {
        ans += (map[num + k] || 0) + (map[num - k] || 0)
        map[num] = (map[num] || 0) + 1
    }
    return ans
}
// @lc code=end
