function countSegments(s: string): number {
  const sTrim = s.trim()
  return sTrim.length ? sTrim.split(/\s+/).length : 0
}
