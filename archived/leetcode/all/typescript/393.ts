function validUtf8(data: number[]): boolean {
  // 0: x < 128, 10: 128 <= x < 192, 11: 192 <= x < 224, 111: 224 <= x < 240, 1111: 240<= x < 248
  const len = data.length
  for (let i = 0; i < len; i++) {
    const dt = data[i]
    if ((dt >= 128 && dt < 192) || dt >= 248) return false
    else if (dt < 128) continue
    // dt >= 192 &&
    else if (dt < 224) {
      if (i + 1 >= len) return false
      if (data[i + 1] < 128 || data[i + 1] >= 192) return false
      i += 1
    }
    // dt >= 224 &&
    else if (dt < 240) {
      if (i + 2 >= len) return false
      for (let j = 1; j <= 2; j++)
        if (data[i + j] < 128 || data[i + j] >= 192) return false
      i += 2
    }
    // dt >= 240 &&
    else if (dt < 248) {
      if (i + 3 >= len) return false
      for (let j = 1; j <= 3; j++)
        if (data[i + j] < 128 || data[i + j] >= 192) return false
      i += 3
    }
  }
  return true
}

// or simulation
