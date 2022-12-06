function stoneGameVI(aliceValues: number[], bobValues: number[]): number {
  let sum = 0
  aliceValues
    .map((v, i) => [i, v + bobValues[i]])
    .sort((a, b) => b[1] - a[1])
    .forEach((v, i) => {
      if (i % 2) {
        sum -= bobValues[v[0]]
      } else {
        sum += aliceValues[v[0]]
      }
    })
  return sum > 0 ? 1 : sum === 0 ? 0 : -1
}
