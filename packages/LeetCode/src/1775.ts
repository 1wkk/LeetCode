function minOperations(nums1: number[], nums2: number[]): number {
  const n1 = nums1.length
  const n2 = nums2.length
  if (Math.min(n1, n2) * 6 < Math.max(n1, n2) * 1) return -1

  const sum1 = nums1.reduce((a, b) => a + b)
  const sum2 = nums2.reduce((a, b) => a + b)

  if (sum1 > sum2) {
    ;[nums1, nums2] = [nums2, nums1]
  }

  let diff = Math.abs(sum1 - sum2)

  const changes = new Array(10).fill(0)
  nums1.forEach((num1) => changes[6 - num1]++)
  nums2.forEach((num2) => changes[num2 - 1]++)

  let ans = 0

  for (let i = 5; i >= 1; i--) {
    if (i * changes[i] >= diff) return ans + Math.ceil(diff / i)

    ans += changes[i]
    diff -= i * changes[i]
  }
}
