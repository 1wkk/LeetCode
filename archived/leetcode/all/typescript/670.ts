function maximumSwap(num: number): number {
  const ns = num.toString().split('')
  const n = ns.length
  let l = -1,
    r = -1,
    _max = n - 1
  for (let i = n - 1; i >= 0; i--) {
    if (ns[i] > ns[_max]) {
      _max = i
    } else if (ns[i] < ns[_max]) {
      l = i
      r = _max
    }
  }
  if (l !== -1) {
    ex(ns, l, r)
  }
  return parseInt(ns.join(''))
}

const ex = (a: Array<number | string>, l: number, r: number) => {
  const c = a[l]
  a[l] = a[r]
  a[r] = c
}
