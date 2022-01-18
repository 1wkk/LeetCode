function numFriendRequests(ages: number[]): number {
  const len = ages.length
  let l = 0,
    r = 0,
    ans = 0

  ages.sort((a, b) => a - b)

  for (const age of ages) {
    if (age < 15) continue
    while (ages[l] <= 0.5 * age + 7) l++
    while (r + 1 < len && ages[r + 1] <= age) r++

    ans += r - l
  }
  return ans
}
