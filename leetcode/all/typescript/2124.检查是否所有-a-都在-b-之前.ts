/*
 * @lc app=leetcode.cn id=2124 lang=typescript
 *
 * [2124] 检查是否所有 A 都在 B 之前
 */

// @lc code=start
function checkString(s: string): boolean {
  let a = -1,
    b = 100
  for (let i = 0; i < s.length; i++) {
    if (s[i] === 'a') a = i
    else if (b === 100) b = i
  }
  return a < b
}
// @lc code=end
