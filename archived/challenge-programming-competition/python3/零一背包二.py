from cmath import inf
from sys import stdin

# 千万注意下标对齐
n, t = map(int, stdin.readline().split())
w = [0 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]
max_v = -inf
for i in range(n):
    w[i + 1], v[i + 1] = map(int, stdin.readline().split())
    max_v = max(max_v, v[i + 1])

dp = [[inf for _ in range(n * max_v + 1)] for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(n * max_v + 1):
        if j < v[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])
ans = 0
for i in range(n * max_v + 1):
    if dp[n][i] <= t:
        ans = i
print(ans)
