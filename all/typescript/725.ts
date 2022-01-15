// Definition for singly-linked list.
class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }
}

function splitListToParts(head: ListNode | null, k: number): Array<ListNode | null> {
  let len = 0
  let temp = head
  while (temp !== null) {
    len += 1
    temp = temp.next
  }
  const num = ~~(len / k)
  const remain = len % k
  const ans = new Array(k).fill(null)
  let cur = head
  for (let i = 0; i < k && cur != null; i++) {
    ans[i] = cur
    const curLen = num + (i < remain ? 1 : 0)
    for (let j = 1; j < curLen; j++) {
      cur = cur.next
    }
    const next = cur.next
    cur.next = null
    cur = next
  }
  return ans
}
