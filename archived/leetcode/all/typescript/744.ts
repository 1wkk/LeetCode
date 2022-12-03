function nextGreatestLetter(letters: string[], target: string): string {
  for (const c of letters) {
    if (c > target) return c
  }
  return letters[0]
}
