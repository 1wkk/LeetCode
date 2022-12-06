function boxDelivering(
  boxes: number[][],
  portsCount: number,
  maxBoxes: number,
  maxWeight: number
): number {
  const n = boxes.length
  // ws[i] 表示包含 i 的重量前缀和，i 从 1 开始
  const ws = new Array(n + 3).fill(0)
  // rs[i] 表示从第 1 个箱子到第 i 个箱子所需的行程，i 从 1 开始
  const rs = new Array(n + 3).fill(0)
  for (let i = 0; i < n; i++) {
    const [p, w] = boxes[i]
    ws[i + 1] = ws[i] + w
    if (i >= 1) {
      const [p2, w2] = boxes[i - 1]
      rs[i + 1] = rs[i] + (p2 != p ? 1 : 0)
    }
  }

  const dp = new Array(n + 3).fill(0)
  // 从朴素中可以看出 dp[i] = rs[i] + 2 + (dp[j] - rs[j + 1])，只与 j 有关
  // 划窗维护 dp[j] - rs[j + 1] 的最小值
  // for (let i = 1; i <= n; i++) {
  //   dp[i] = Infinity
  //   for (let j = Math.max(0, i - maxBoxes); j < i; j++) {
  //     if (ws[i] - ws[j] <= maxWeight) {
  //       dp[i] = Math.min(dp[i], dp[j] + (rs[i] - rs[j + 1]) + 2)
  //     }
  //   }
  // }

  // 划窗/单调队列，存储最优解的下标
  const q = [0]
  for (let i = 1; i <= n; i++) {
    while (q.length && (i - q[0] > maxBoxes || ws[i] - ws[q[0]] > maxWeight)) {
      q.shift()
    }
    if (q.length) {
      dp[i] = rs[i] + 2 + (dp[q[0]] - rs[q[0] + 1])
    }
    if (i < n) {
      // 当前队尾不是最优解
      while (
        q.length &&
        dp[q[q.length - 1]] - rs[q[q.length - 1] + 1] >= dp[i] - rs[i + 1]
      ) {
        q.pop()
      }
      q.push(i)
    }
  }

  return dp[n]
}
