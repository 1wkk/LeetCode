from sys import stdin


m, n = map(int, stdin.readline().split())
s = stdin.readline()
t = stdin.readline()

dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(m):
    for j in range(n):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[m][n])
