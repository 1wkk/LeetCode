/*
 * @lc app=leetcode.cn id=2125 lang=typescript
 *
 * [2125] 银行中的激光束数量
 */

// @lc code=start
function numberOfBeams(bank: string[]): number {
  let cnts = new Array(bank.length).fill(0)
  for (let i = 0; i < bank.length; i++) {
    for (let j = 0; j < bank[i].length; j++) {
      if (bank[i][j] === '1') cnts[i]++
    }
  }
  cnts = cnts.filter(v => v !== 0)
  if (cnts.length === 1) return 0
  let res = 0
  for (let i = 1; i < cnts.length; i++) {
    res += cnts[i - 1] * cnts[i]
  }
  return res
}
// @lc code=end
