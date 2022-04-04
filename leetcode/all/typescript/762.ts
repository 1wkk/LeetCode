function countPrimeSetBits(l: number, r: number): number {
  const bitCount = (x: number) => {
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    return (((x + (x >> 4)) & 0xf0f0f0f) * 0x1010101) >> 24
  }
  const isPrime = (x: number) => {
    if (x < 2) return false
    for (let i = 2; i * i <= x; i++) if (x % i === 0) return false
    return true
  }

  let ans = 0
  for (let i = l; i <= r; i++) if (isPrime(bitCount(i))) ans++
  return ans
}
