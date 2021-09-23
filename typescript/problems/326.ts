function isPowerOfThree(n: number): boolean {
  // while (n && n % 3 === 0) {
  //   n /= 3
  // }
  // return n === 1
  return n > 0 && 1162261467 % n === 0
}
