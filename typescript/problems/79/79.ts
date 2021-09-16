function exist(board: string[][], word: string): boolean {
  const row = board.length
  const col = board[0].length
  const directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
  ]
  const visited = new Array(row)
    .fill(false)
    .map(a => new Array<boolean>(col).fill(false))

  const inArea = (x: number, y: number) =>
    x >= 0 && x < row && y >= 0 && y < col

  const find = (x: number, y: number, idx: number) => {
    if (board[x][y] !== word[idx]) {
      return false
    } else if (idx === word.length - 1) {
      return true
    }
    visited[x][y] = true
    let res = false
    for (const [dx, dy] of directions) {
      let nx = x + dx,
        ny = y + dy
      if (inArea(nx, ny) && !visited[nx][ny] && find(nx, ny, idx + 1)) {
        res = true
        break
      }
    }
    visited[x][y] = false
    return res
  }
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (find(i, j, 0)) {
        return true
      }
    }
  }
  return false
}
