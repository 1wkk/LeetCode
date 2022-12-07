function squareIsWhite(coordinates: string): boolean {
  return (
    (coordinates[0].charCodeAt(0) - 'a'.charCodeAt(0)) % 2 ===
    (coordinates[1].charCodeAt(0) - '0'.charCodeAt(0)) % 2
  )
}
