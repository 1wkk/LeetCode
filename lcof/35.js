/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
  const map = new Map()
  for (let cur = head; cur; cur = cur.next) {
    map.set(cur, new Node(cur.val))
  }
  for (let cur = head; cur; cur = cur.next) {
    map.get(cur).next = map.get(cur.next) ?? null
    map.get(cur).random = map.get(cur.random) ?? null
  }
  return map.get(head) ?? null
}
