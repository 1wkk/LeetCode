function longestCommonPrefix(strs: string[]): string {
  strs.sort()
  const str_1 = strs[0]
  const str_2 = strs[strs.length - 1]
  let ans = ''
  for (let i = 0; i < Math.min(str_1.length, str_2.length); i++) {
    if (str_1[i] !== str_2[i]) break
    ans += str_1[i]
  }
  return ans
}
