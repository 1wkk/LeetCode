function missingNumber(nums: number[]): number {
  let l = 0,
    r = nums.length - 1
  while (l <= r) {
    const m = l + ~~((r - l) / 2)
    if (m === nums[m]) l = m + 1
    else r = m - 1
  }
  return l
}
