/*
 * @lc app=leetcode.cn id=2029 lang=typescript
 *
 * [2029] 石子游戏 IX
 *
 * 博弈论
 */

// @lc code=start
function stoneGameIX(stones: number[]): boolean {
  const s = [0, 0, 0]
  for (const stone of stones) s[stone % 3]++

  const check = (a: number, b: number, c: number) => {
    // 如果只有 0 和另外一种石子，Alice 必输
    if (b === 0) return false
    // 取第一个石子
    b--
    // 回合数
    let turn = 1 + Math.min(b, c) * 2 + a
    // 末尾可以再接一个 1 or 2
    if (b > c) {
      turn++
      b--
    }
    // 回合数为奇数且还有剩余石子
    return turn % 2 === 1 && b !== c
  }

  return check(s[0], s[1], s[2]) || check(s[0], s[2], s[1])
}
// @lc code=end
