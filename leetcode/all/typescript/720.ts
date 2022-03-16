function longestWord(words: string[]): string {
  words.sort((a, b) => {
    if (a.length !== b.length) {
      return a.length - b.length
    }
    return b.localeCompare(a)
  })
  let ans = ''
  const set = new Set([''])
  for (const word of words) {
    if (set.has(word.substring(0, word.length - 1))) {
      set.add(word)
      ans = word
    }
  }
  return ans
}
