function findRepeatNumber(nums: number[]): number {
  let i = 0
  while (i < nums.length) {
    const idx = nums[i]
    if (i !== idx) {
      if (idx === nums[idx]) return idx
      nums[i] = nums[idx]
      nums[idx] = idx
    } else i++
  }
  return -1
}
