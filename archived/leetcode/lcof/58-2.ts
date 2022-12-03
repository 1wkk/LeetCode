function reverseLeftWords(s: string, n: number): string {
  return `${s.substring(n)}${s.substr(0, n)}`
}
