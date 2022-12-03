class NumArray {
  nums: number[]
  f: number[]
  constructor(nums: number[]) {
    this.nums = nums
    this.f = new Array(nums.length * 4 + 1).fill(0)

    const build = (k, l, r) => {
      if (l === r) {
        this.f[k] = nums[l - 1]
        return
      }
      const m = (l + r) >> 1
      build(2 * k, l, m)
      build(2 * k + 1, m + 1, r)
      this.f[k] = this.f[2 * k] + this.f[2 * k + 1]
    }

    build(1, 1, nums.length)
  }

  update(i: number, v: number): void {
    const vv = v - this.nums[i]
    this.nums[i] = v
    const add = (k, l, r, i, v) => {
      this.f[k] += v
      if (l === r) return
      const m = (l + r) >> 1
      if (i <= m) add(2 * k, l, m, i, v)
      else add(2 * k + 1, m + 1, r, i, v)
    }
    add(1, 1, this.nums.length, i + 1, vv)
  }

  sumRange(ll: number, rr: number): number {
    const sum = (k, l, r, ll, rr) => {
      if (l === ll && r === rr) return this.f[k]
      const m = (l + r) >> 1
      if (rr <= m) return sum(2 * k, l, m, ll, rr)
      else {
        if (ll > m) return sum(2 * k + 1, m + 1, r, ll, rr)
        else return sum(2 * k, l, m, ll, m) + sum(2 * k + 1, m + 1, r, m + 1, rr)
      }
    }
    return sum(1, 1, this.nums.length, ll + 1, rr + 1)
  }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * obj.update(index,val)
 * var param_2 = obj.sumRange(left,right)
 */
