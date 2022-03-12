/*
 * @lc app=leetcode.cn id=306 lang=typescript
 *
 * [306] 累加数
 */

// @lc code=start
function isAdditiveNumber(num: string): boolean {
  /**
   * 1 + 2 = 3
   * @param idx
   * @param count 目前有几个数（必须先造出两个数）
   * @param pp 1
   * @param p 2
   * @cur 目前的数（通常作为和来验证），count < 2 时，直接保存
   * @returns
   */
  const dfs = (idx, count, pp, p) => {
    // 有效的 累加序列 必须含有至少三个数
    if (idx >= num.length) {
      return count > 2
    }

    let cur = 0
    for (let i = idx; i < num.length; i++) {
      const c = num[i]
      // 不作为前导0
      if (num[idx] === '0' && i > idx) return false

      cur = cur * 10 + parseInt(c)

      if (count >= 2) {
        let sum = pp + p
        if (cur > sum) return false
        if (cur < sum) continue
      }

      // 1.目前小于两个数，继续造数
      // 2.上述满足了 pp + p = cur，转到此处进行下一组累加序列验证
      if (dfs(i + 1, count + 1, p, cur)) return true
    }

    return false
  }
  return dfs(0, 0, 0, 0)
}
// @lc code=end
