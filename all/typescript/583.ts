function minDistance(word1: string, word2: string): number {
  function longestCommonSubsequence(text1: string, text2: string): number {
    const len1 = text1.length
    const len2 = text2.length
    const dp = new Array(len1 + 1).fill(null).map(() => new Array(len2 + 1).fill(0))
    for (let i = 1; i <= len1; i++) {
      for (let j = 1; j <= len2; j++) {
        if (text1[i - 1] === text2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + 1
        } else {
          dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
        }
      }
    }
    return dp[len1][len2]
  }
  return word1.length + word2.length - 2 * longestCommonSubsequence(word1, word2)
}
