function calPoints(ops: string[]): number {
  const scores = []
  for (const op of ops) {
    if (op === '+') {
      scores.push(scores[scores.length - 1] + scores[scores.length - 2])
    } else if (op === 'D') {
      scores.push(scores[scores.length - 1] * 2)
    } else if (op === 'C') {
      scores.pop()
    } else {
      scores.push(parseInt(op))
    }
  }
  return scores.reduce((sum, v) => (sum += v), 0)
}
