/*
 * @lc app=leetcode.cn id=448 lang=typescript
 *
 * [448] 找到所有数组中消失的数字
 */

// @lc code=start
function findDisappearedNumbers(nums: number[]): number[] {
    const n = nums.length
    for (const num of nums) {
        const x = (num - 1) % n
        nums[x] += n
    }
    const ans = []
    for (const i in nums) if (nums[i] <= n) ans.push(parseInt(i) + 1)
    return ans
}
// @lc code=end
