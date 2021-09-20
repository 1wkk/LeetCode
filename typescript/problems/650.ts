function minSteps(n: number): number {
  const dp = new Array(n + 1).fill(Infinity)
  ;(dp[0] = 0), (dp[1] = 0)
  for (let i = 0; i <= n; i++) {
    for (let j = 1; j * j <= i; j++) {
      if (i % j === 0) {
        dp[i] = min(dp[i], dp[j] + i / j)
        dp[i] = min(dp[i], dp[i / j] + j)
      }
    }
  }
  return dp[n]
}

const min = Math.min
