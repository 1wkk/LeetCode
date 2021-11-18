function search(nums: number[], target: number): number {
  const helper = target => {
    let l = 0,
      r = nums.length - 1
    while (l <= r) {
      const m = l + ~~((r - l) / 2)
      if (nums[m] <= target) l = m + 1
      else r = m - 1
    }
    return l
  }

  return helper(target) - helper(target - 1)
}
