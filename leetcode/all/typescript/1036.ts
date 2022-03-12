/*
 * @lc app=leetcode.cn id=1036 lang=typescript
 *
 * [1036] 逃离大迷宫
 */

// @lc code=start
function isEscapePossible(blocked: number[][], source: number[], target: number[]): boolean {
  const directions = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1]
  ]
  const isVisited: boolean[][] = new Array(10 ^ 6).fill(false).map(() => new Array(10 ^ 6).fill(false))

  const isValid = (x: number, y: number) => {
    for (const block of blocked) {
      if (x === block[0] && y === block[1]) return false
    }
    return x >= 0 && x < (10 ^ 6) && y >= 0 && y < (10 ^ 6) && !isVisited[x][y]
  }

  const foo = (x: number, y: number) => {
    if (x === target[0] && y === target[1]) return true
    for (const dir of directions) {
      const nx = x + dir[0],
        ny = y + dir[1]
      if (isValid(nx, ny) && foo(nx, ny)) return true
    }
    return false
  }
  return foo(source[0], source[1])
}
// @lc code=end
