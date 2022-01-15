/*
 * @lc app=leetcode.cn id=313 lang=typescript
 *
 * [313] 超级丑数
 */

// @lc code=start
function nthSuperUglyNumber(n: number, primes: number[]): number {
  const arr = new Array(n + 1).fill(1)
  const idxs = new Array(primes.length).fill(1)
  for (let i = 2; i <= n; i++) {
    const nums = []
    for (let j = 0; j < primes.length; j++) {
      nums.push(primes[j] * arr[idxs[j]])
    }
    const min = Math.min(...nums)
    for (let j = 0; j < primes.length; j++) {
      if (min === arr[idxs[j]] * primes[j]) idxs[j]++
    }
    arr[i] = min
  }
  return arr[n]
}
// @lc code=end
