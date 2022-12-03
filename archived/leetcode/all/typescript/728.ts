function selfDividingNumbers(left: number, right: number): number[] {
  const ans = []
  for (let i = left; i <= right; i++) {
    let ar = i
    while (ar) {
      const re = ar % 10
      if (re === 0 || i % re !== 0) break
      ar = ~~(ar / 10)
    }
    if (ar <= 0) ans.push(i)
  }
  return ans
}
