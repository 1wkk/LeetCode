from cmath import inf

h, w = map(int, input().split())
g = [[] for _ in range(h)]
for i in range(h):
    g[i] = input()
dp = [[inf for _ in range(w)] for _ in range(h)]
dp[0][0] = 1 if g[0][0] == '#' else 0
for i in range(1, w):
    if g[0][i] == '.':
        dp[0][i] = dp[0][i - 1]
    else:
        if g[0][i - 1] == '#':
            dp[0][i] = dp[0][i - 1]
        else:
            dp[0][i] = dp[0][i - 1] + 1
for i in range(1, h):
    if g[i][0] == '.':
        dp[i][0] = dp[i - 1][0]
    else:
        if g[i - 1][0] == '#':
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = dp[i - 1][0] + 1
for i in range(1, h):
    for j in range(1, w):
        if g[i][j] == '.':
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
        else:
            if g[i - 1][j] == '#':
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + 1
            if g[i][j - 1] == '#':
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
print(dp[h - 1][w - 1])
