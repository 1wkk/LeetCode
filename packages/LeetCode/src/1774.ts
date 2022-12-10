function closestCost(
  baseCosts: number[],
  toppingCosts: number[],
  t: number
): number {
  let a = Infinity

  const dfs = (c, i) => {
    // 剪枝，但是不剪左边
    if (c - t > abs(a - t)) return

    if (abs(c - t) < abs(a - t)) {
      a = c
    }

    if (abs(c - t) === abs(a - t)) {
      a = min(a, c)
    }

    if (i >= toppingCosts.length) return

    dfs(c, i + 1)
    dfs(c + toppingCosts[i], i + 1)
    dfs(c + 2 * toppingCosts[i], i + 1)
  }

  for (const b of baseCosts) {
    dfs(b, 0)
  }

  return a
}

// --

const min = Math.min
const max = Math.max
const abs = Math.abs
