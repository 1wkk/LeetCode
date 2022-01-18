/*
 * @lc app=leetcode.cn id=2127 lang=typescript
 *
 * [2127] 参加会议的最多员工数
 */

// @lc code=start
// https://leetcode-cn.com/problems/maximum-employees-to-be-invited-to-a-meeting/solution/javascript-yi-ge-hao-dong-dian-de-si-lu-k4zu3/
function maximumInvitations(favs: number[]): number {
  const len = favs.length
  // indegree array
  const indegrees = new Array(len).fill(0)
  for (const fav of favs) indegrees[fav]++

  let queue = []
  for (let i = 0; i < len; i++) {
    if (indegrees[i] === 0) queue.push(i)
  }

  // store the length of graph, which through by i
  const h = new Array(len).fill(1)

  // from which indegree = 0
  while (queue.length) {
    let tep = []
    for (const x of queue) {
      const fav = favs[x]
      h[fav] = Math.max(h[fav], h[x] + 1)
      if (--indegrees[fav] === 0) tep.push(fav)
    }
    queue = tep
  }

  const vis = {}
  let res = 0,
    hs = 0
  for (let i = 0; i < len; i++) {
    if (vis[i] || !indegrees[i]) continue
    let cur = i,
      l = 0
    while (!vis[cur]) {
      l++
      vis[cur] = true
      cur = favs[cur]
    }
    res = Math.max(res, l)

    if (l === 2) hs += h[i] + h[favs[i]]
  }

  return Math.max(res, hs)
}
// @lc code=end
