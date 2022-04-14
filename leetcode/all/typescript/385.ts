/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     If value is provided, then it holds a single integer
 *     Otherwise it holds an empty nested list
 *     constructor(value?: number) {
 *         ...
 *     };
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     isInteger(): boolean {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     getInteger(): number | null {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     setInteger(value: number) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     add(elem: NestedInteger) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds,
 *     or an empty list if this NestedInteger holds a single integer
 *     getList(): NestedInteger[] {
 *         ...
 *     };
 * };
 */

// @ts-ignore
function deserialize(s: string): NestedInteger {
  // @ts-ignore
  if (s[0] !== '[') return new NestedInteger(parseInt(s))

  const stack = []
  let num = 0,
    negative = false
  for (let i = 0; i < s.length; i++) {
    const c = s[i]
    if (c === '-') negative = true
    else if (Number.isInteger(parseInt(c))) num = num * 10 + parseInt(c)
    // @ts-ignore
    else if (c === '[') stack.push(new NestedInteger())
    else if (c === ']' || c === ',') {
      if (Number.isInteger(parseInt(s[i - 1]))) {
        if (negative) {
          num *= -1
          negative = false
        }
        // @ts-ignore
        stack[stack.length - 1].add(new NestedInteger(num))
        num = 0
      }
      if (c === ']' && stack.length > 1) {
        const ni = stack.pop()
        stack[stack.length - 1].add(ni)
      }
    }
  }
  return stack.pop()
}
