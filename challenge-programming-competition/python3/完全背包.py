from sys import stdin

# 千万注意下标对齐
n, t = map(int, stdin.readline().split())
w = [0 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]
for i in range(n):
    w[i + 1], v[i + 1] = map(int, stdin.readline().split())


# dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(t + 1):
#         if j < w[i]:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             # 次数为 dp[i][j - w[i]] + v[i] 的解释：当前状态为选取了 k 个下标为 i 的物品，
#             # dp[i][j] 是从 选取了 k - 1 个下标为 i 的物品而来，所以不用 i - 1
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - w[i]] + v[i])
# print(dp[n][t])


# dp = [0 for _ in range(t + 1)]
# for i in range(1, n + 1):
#     for j in range(w[i], t + 1):
#         # 正序是为了保证使用的是同一维的数据
#         dp[j] = max(dp[j], dp[j - w[i]] + v[i])
# print(dp[t])


# 滚动数组
dp = [[0 for _ in range(t + 1)] for _ in range(2)]
for i in range(1, n + 1):
    for j in range(t + 1):
        if j < w[i]:
            dp[i & 1][j] = dp[(i - 1) & 1][j]
        else:
            # 次数为 dp[i][j - w[i]] + v[i] 的解释：当前状态为选取了 k 个下标为 i 的物品，
            # dp[i][j] 是从 选取了 k - 1 个下标为 i 的物品而来，所以不用 i - 1
            dp[i & 1][j] = max(dp[(i - 1) & 1][j], dp[i & 1][j - w[i]] + v[i])
print(dp[n & 1][t])
