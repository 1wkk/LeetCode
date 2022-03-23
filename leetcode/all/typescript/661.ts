function imageSmoother(img: number[][]): number[][] {
  const r = img.length,
    c = img[0].length
  const calc = (x, y) => {
    let sum = 0,
      cnt = 0
    for (let i = -1; i <= 1; i++) {
      for (let j = -1; j <= 1; j++) {
        const xi = x + i,
          yj = y + j
        if (xi >= 0 && xi < r && yj >= 0 && yj < c) {
          sum += img[xi][yj]
          cnt += 1
        }
      }
    }
    return ~~(sum / cnt)
  }
  const ans = new Array(r).fill(0).map(() => new Array(c).fill(0))
  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      ans[i][j] = calc(i, j)
    }
  }
  return ans
}
