function twoSum(nums: number[], target: number): number[] {
  const map = new Map()
  for (const [idx, num] of nums.entries()) {
    if (map.has(target - num)) {
      return [idx, map.get(target - num)]
    }
    map.set(num, idx)
  }
}
