/*
 * @lc app=leetcode.cn id=264 lang=typescript
 *
 * [264] 丑数 II
 */

// @lc code=start
function nthUglyNumber(n: number): number {
  const ans = new Array(n + 1).fill(1)
  for (let i2 = 1, i3 = 1, i5 = 1, i = 2; i <= n; i++) {
    let a = ans[i2] * 2,
      b = ans[i3] * 3,
      c = ans[i5] * 5
    const min = Math.min(a, b, c)
    if (min === a) i2++
    if (min === b) i3++
    if (min === c) i5++
    ans[i] = min
  }
  return ans[n]
}
// @lc code=end
