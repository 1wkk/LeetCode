class CQueue {
  stackIn: number[]
  stackOut: number[]

  constructor() {
    this.stackIn = []
    this.stackOut = []
  }

  appendTail(value: number): void {
    this.stackIn.push(value)
  }

  deleteHead(): number {
    if (this.stackOut.length) return this.stackOut.pop()
    if (!this.stackIn.length) return -1

    while (this.stackIn.length) this.stackOut.push(this.stackIn.pop())
    return this.stackOut.pop()
  }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
