function checkPowersOfThree(n: number): boolean {
  while (n) {
    if (n % 3 > 1) {
      return false
    }
    n = ~~(n / 3)
  }
  return true
}
