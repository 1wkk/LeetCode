class NumArray {
  nums: number[]
  tree: number[]
  constructor(nums: number[]) {
    this.nums = nums
    this.tree = new Array(nums.length + 1).fill(0)
    for (let i = 0; i < nums.length; i++) {
      this.add(i + 1, nums[i])
    }
  }

  update(index: number, val: number): void {
    this.add(index + 1, val - this.nums[index])
    this.nums[index] = val
  }

  sumRange(left: number, right: number): number {
    return this.prefixSum(right + 1) - this.prefixSum(left)
  }

  lowBit = x => x & -x

  add(idx, v) {
    while (idx < this.tree.length) {
      this.tree[idx] += v
      idx += this.lowBit(idx)
    }
  }

  prefixSum(idx) {
    let sum = 0
    while (idx > 0) {
      sum += this.tree[idx]
      idx -= this.lowBit(idx)
    }
    return sum
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */
