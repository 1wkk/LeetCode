/*
 * @lc app=leetcode.cn id=1001 lang=typescript
 *
 * [1001] 网格照明
 */

// @lc code=start
function gridIllumination(n: number, lamps: number[][], queries: number[][]): number[] {
    const points = new Set()
    const row = {},
        col = {},
        diag = {},
        antiDiag = {}
    for (const [r, c] of lamps) {
        if (!points.has(`${r}, ${c}`)) {
            points.add(`${r}, ${c}`)
            row[r] = (row[r] || 0) + 1
            col[c] = (col[c] || 0) + 1
            diag[r - c] = (diag[r - c] || 0) + 1
            antiDiag[r + c] = (antiDiag[r + c] || 0) + 1
        }
    }
    const ans = []
    for (const [r, c] of queries) {
        console.log(row[r], col[c], diag[r - c], antiDiag[r + c])
        if (row[r] || col[c] || diag[r - c] || antiDiag[r + c]) ans.push(1)
        else ans.push(0)
        for (let x = r - 1; x <= r + 1; x++) {
            for (let y = c - 1; y <= c + 1; y++) {
                if (points.has(`${x}, ${y}`)) {
                    points.delete(`${x}, ${y}`)
                    row[x] = (row[x] || 0) - 1
                    col[y] = (col[y] || 0) - 1
                    diag[x - y] = (diag[x - y] || 0) - 1
                    antiDiag[x + y] = (antiDiag[x + y] || 0) - 1
                }
            }
        }
    }
    return ans
}
// @lc code=end
