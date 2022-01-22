/*
 * @lc app=leetcode.cn id=1332 lang=typescript
 *
 * [1332] 删除回文子序列
 */

// @lc code=start
function removePalindromeSub(s: string): number {
  let l = 0,
    r = s.length - 1
  while (l < r) {
    if (s[l++] !== s[r--]) return 2
  }
  return 1
}
// @lc code=end
