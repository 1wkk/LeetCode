function countConsistentStrings(allowed: string, words: string[]): number {
  return words.filter((w) => w.split('').every((c) => allowed.includes(c)))
    .length
}
