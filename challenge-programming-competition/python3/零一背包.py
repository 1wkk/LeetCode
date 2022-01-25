from sys import stdin

# 千万注意下标对齐
n, t = map(int, stdin.readline().split())
w = [0 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]
for i in range(n):
    w[i + 1], v[i + 1] = map(int, stdin.readline().split())


# 二维数组写法 易于理解

# dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(t + 1):
#         if j < w[i]:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
# print(dp[n][t])


# 一维数组写法 优化空间
# `j` 倒序写法的解释：
# 从二维数组写法得知，dp[j - w[i]] 应为 i - 1 的数据，倒序写法可以保证当前一维是从上一维更新而来！！！

# dp = [0 for _ in range(t + 1)]

# for i in range(1, n + 1):
#     for j in range(t, w[i] - 1, -1):
#         dp[j] = max(dp[j], dp[j - w[i]] + v[i])
# print(dp[t])


# 滚动数组

dp = [[0 for _ in range(t + 1)] for _ in range(2)]
for i in range(1, n + 1):
    for j in range(t + 1):
        if j < w[i]:
            dp[i & 1][j] = dp[(i - 1) & 1][j]
        else:
            dp[i & 1][j] = max(dp[(i - 1) & 1][j], dp[(i - 1) & 1][j - w[i]] + v[i])
print(dp[n & 1][t])
