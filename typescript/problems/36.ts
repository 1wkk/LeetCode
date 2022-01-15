const getAscii = (c: string) => c.charCodeAt(0)

const ASCII_ZERO = getAscii('0')

function isValidSudoku(board: string[][]): boolean {
  const rows = new Array(9).fill(0).map(() => new Array(9).fill(0))
  const cols = new Array(9).fill(0).map(() => new Array(9).fill(0))
  const boxes = new Array(3).fill(0).map(() => new Array(3).fill(0).map(() => new Array(9).fill(0)))

  const row = board.length
  const col = board[0].length
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      const c = board[i][j]
      if (c !== '.') {
        const idx = getAscii(c) - ASCII_ZERO - 1
        if (++rows[i][idx] > 1 || ++cols[j][idx] > 1 || ++boxes[~~(i / 3)][~~(j / 3)][idx] > 1) {
          return false
        }
      }
    }
  }
  return true
}
