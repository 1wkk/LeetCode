function missingRolls(rolls: number[], mean: number, n: number): number[] {
  const remain =
    mean * (rolls.length + n) - rolls.reduce((_sum, roll) => (_sum += roll), 0)
  const miss = []
  if (n <= remain && remain <= 6 * n) {
    const ave = ~~(remain / n),
      sc = remain % n
    for (let i = 0; i < n; i++) miss.push(ave + (i < sc ? 1 : 0))
  }
  return miss
}
