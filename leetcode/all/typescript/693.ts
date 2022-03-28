function hasAlternatingBits(n: number): boolean {
  let last = -1
  while (n) {
    if (last === n % 2) return false
    last = n % 2
    n = ~~(n / 2)
  }
  return true
}
