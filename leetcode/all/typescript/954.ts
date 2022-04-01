const abs = Math.abs

function canReorderDoubled(arr: number[]): boolean {
  const cnt = new Map()
  for (const x of arr) cnt.set(x, (cnt.get(x) || 0) + 1)

  if ((cnt.get(0) || 0) % 2 !== 0) return false

  const vals = []
  for (const x of cnt.keys()) vals.push(x)
  vals.sort((a, b) => abs(a) - abs(b))

  for (const x of vals) {
    if ((cnt.get(2 * x) || 0) < cnt.get(x)) return false

    cnt.set(2 * x, (cnt.get(2 * x) || 0) - cnt.get(x))
  }
  return true
}
