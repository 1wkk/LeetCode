/*
 * @lc app=leetcode.cn id=2094 lang=typescript
 *
 * [2094] 找出 3 位偶数
 */

// @lc code=start
function findEvenNumbers(digits: number[]): number[] {
  const res = []
  const fre = new Array(10).fill(0)
  for (const digit of digits) fre[digit]++

  for (let i = 100; i < 1000; i += 2) {
    const fre2 = new Array(10).fill(0)
    let alt = i
    let flag = true

    while (alt) {
      const re = alt % 10

      fre2[re]++
      if (fre2[re] > fre[re]) {
        flag = false
        break
      }

      alt = ~~(alt / 10)
    }

    if (flag) res.push(i)
  }

  return res
}
// @lc code=end
