function countMaxOrSubsets(nums: number[]): number {
  let $max = 0,
    ans = 0
  const $len = nums.length
  for (const num of nums) $max |= num

  const backtrack = (idx, $sum) => {
    if (idx === $len) {
      ans += $sum === $max ? 1 : 0
      return
    }
    backtrack(idx + 1, $sum)
    backtrack(idx + 1, ($sum |= nums[idx]))
  }

  backtrack(0, 0)
  return ans
}
