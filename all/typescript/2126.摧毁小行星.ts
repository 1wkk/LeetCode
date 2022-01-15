/*
 * @lc app=leetcode.cn id=2126 lang=typescript
 *
 * [2126] 摧毁小行星
 */

// @lc code=start
function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
  asteroids.sort((a, b) => a - b)
  // console.log(asteroids)
  for (let i = 0; i < asteroids.length; i++) {
    const ast = asteroids[i]
    if (mass < ast) return false
    else mass += ast
  }
  return true
}
// @lc code=end
