function findLongestWord(s: string, dictionary: string[]): string {
  dictionary.sort((a, b) =>
    a.length === b.length ? a.localeCompare(b) : b.length - a.length
  )
  for (const w of dictionary) {
    let i = 0,
      j = 0
    while (i < w.length && j < s.length) {
      if (w[i] === s[j]) {
        i++
      }
      j++
    }
    if (i === w.length) {
      return w
    }
  }
  return ''
}
