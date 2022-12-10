function minOperations(nums: number[]): number {
  let ans = 0
  const n = nums.length
  for (let i = 1; i < n; i++) {
    if (nums[i] > nums[i - 1]) continue
    else {
      ans += nums[i - 1] + 1 - nums[i]
      nums[i] = nums[i - 1] + 1
    }
  }
  return ans
}
