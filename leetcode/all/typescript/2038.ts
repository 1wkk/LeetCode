function winnerOfGame(colors: string): boolean {
  let a = 0,
    b = 0,
    cc = '',
    count = 0
  for (const c of colors) {
    if (c !== cc) {
      cc = c
      count = 1
    } else {
      count += 1
      if (count >= 3) {
        if (cc === 'A') a += 1
        else b += 1
      }
    }
  }
  return a > b
}
