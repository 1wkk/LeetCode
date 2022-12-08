function countNicePairs(nums: number[]): number {
  let ans = 0
  const map = new Map()
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    const diff = num - rev(num)

    if (map.has(diff)) {
      ans = (ans + map.get(diff)) % 1000000007
    }

    map.set(diff, (map.get(diff) || 0) + 1)
  }
  return ans
}

const revMap = new Map()

const rev = (_i: number) => {
  if (revMap.has(_i)) return revMap.get(_i)

  let i = _i
  let ii = 0
  while (i) {
    ii = ii * 10 + (i % 10)
    i = ~~(i / 10)
  }

  revMap.set(_i, ii)

  return ii
}
