function trailingZeroes(n: number): number {
  let ans = 0
  while (n !== 0) {
    n = ~~(n / 5)
    ans += n
  }
  return ans
}
