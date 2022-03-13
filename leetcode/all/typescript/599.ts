function findRestaurant(list1: string[], list2: string[]): string[] {
  let ans = []
  const map = new Map()
  for (let i = 0; i < list1.length; i++) map.set(list1[i], i)
  let $min = Infinity
  for (let i = 0; i < list2.length; i++) {
    const k = list2[i]
    if (map.has(k)) {
      map.set(k, map.get(k) + i)
      if (map.get(k) < $min) {
        ans = [k]
        $min = map.get(k)
      } else if (map.get(k) === $min) ans.push(k)
    }
  }
  return ans
}
