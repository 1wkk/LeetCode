function lengthOfLIS(nums: number[]): number {
  const len = nums.length
  const dp = new Array(len).fill(1)
  let ans = 1
  for (let i = 1; i < len; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) {
        dp[i] = max(dp[i], dp[j] + 1)
      }
    }
    ans = max(ans, dp[i])
  }
  return ans
}

const max = Math.max
