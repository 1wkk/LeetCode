/*
 * @lc app=leetcode.cn id=1716 lang=typescript
 *
 * [1716] 计算力扣银行的钱
 */

// @lc code=start
// 模拟
function totalMoney(n: number): number {
  let ans = 0
  // 1 + ~~((i - 1) / 7) 每周一的钱
  // (i - 1) % 7 每周的第二天开始加钱
  for (let i = 1; i <= n; i++) ans += 1 + ~~((i - 1) / 7) + ((i - 1) % 7)
  return ans
}
// @lc code=end
