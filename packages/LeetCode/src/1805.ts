function numDifferentIntegers(word: string): number {
  return [
    ...new Set(
      word
        .split(/[a-zA-Z]/)
        .filter((v) => v.length)
        .map((v) => v.replace(/^0+/, ''))
    ),
  ].length
}
