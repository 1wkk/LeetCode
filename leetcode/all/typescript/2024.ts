function maxConsecutiveAnswers(answerKey: string, k: number): number {
  const n = answerKey.length

  const cal = c => {
    let ans = 0
    for (let l = 0, r = 0, $sum = 0; r < n; r++) {
      $sum += answerKey[r] !== c ? 1 : 0
      while ($sum > k) $sum -= answerKey[l++] !== c ? 1 : 0
      ans = Math.max(ans, r - l + 1)
    }
    return ans
  }

  return Math.max(cal('T'), cal('F'))
}
