function maxHeight(cuboids: number[][]): number {
  cuboids.forEach((cuboid) => cuboid.sort((a, b) => a - b))
  cuboids.sort((a, b) => {
    const n = a.length
    for (let i = 0; i < n; i++) {
      if (a[i] !== b[i]) return a[i] - b[i]
    }
  })
  let ans = -1
  const n = cuboids.length
  const dp = new Array(n).fill(0)
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (cuboids[j][1] <= cuboids[i][1] && cuboids[j][2] <= cuboids[i][2]) {
        dp[i] = Math.max(dp[i], dp[j])
      }
    }
    dp[i] += cuboids[i][2]
    ans = Math.max(ans, dp[i])
  }
  return ans
}
