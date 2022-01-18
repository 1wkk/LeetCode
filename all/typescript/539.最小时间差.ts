/*
 * @lc app=leetcode.cn id=539 lang=typescript
 *
 * [539] 最小时间差
 */

// @lc code=start
function findMinDifference(timePoints: string[]): number {
  const ans = []
  for (const timePoint of timePoints) {
    const h = parseInt(timePoint.substring(0, 2))
    const m = parseInt(timePoint.substring(3))
    ans.push(h * 60 + m)
    ans.push(h * 60 + m + 24 * 60)
  }
  // console.log(ans)
  // Array.sort 影响数组本身，并且默认是按照字符串排序（字典序）
  ans.sort((a, b) => a - b)
  // console.log(ans)
  let min = Infinity
  for (let i = 1; i < ans.length; i++) {
    const t1 = ans[i]
    const t2 = ans[i - 1]
    min = Math.min(min, t1 - t2)
  }
  return min
}
// @lc code=end
