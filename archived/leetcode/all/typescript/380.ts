class RandomizedSet {
  list: number[] = []
  map = new Map<number, number>()

  constructor() {}

  insert(val: number): boolean {
    if (this.map.has(val)) return false
    this.map.set(val, this.list.length)
    this.list.push(val)
    return true
  }

  remove(val: number): boolean {
    if (!this.map.has(val)) return false
    const i = this.map.get(val)
    this.list[i] = this.list[this.list.length - 1]
    this.list.pop()
    this.map.set(this.list[i], i)
    this.map.delete(val)
    return true
  }

  getRandom(): number {
    return this.list[~~(Math.random() * this.list.length)]
  }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */
