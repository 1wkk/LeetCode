function getSumAbsoluteDifferences(nums: number[]): number[] {
  const n = nums.length
  const answer = new Array(n)
  const prefixes = new Array(n + 1).fill(0)
  for (let i = 0; i < n; i++) {
    prefixes[i + 1] = prefixes[i] + nums[i]
  }
  for (let i = 0; i < n; i++) {
    const num = nums[i]
    answer[i] =
      num * i -
      prefixes[i] +
      (prefixes[n] - prefixes[i + 1]) -
      num * (n - 1 - i)
  }
  return answer
}
