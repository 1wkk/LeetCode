from bisect import bisect_left
from cmath import inf
from sys import stdin


input = stdin.readline

n = int(input())
a = [int(t) for t in input().split()]

# dp = [1 for _ in range(n)]
# ans = 0

# for i in range(n):
#     for j in range(i):
#         if a[j] < a[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
#     ans = max(ans, dp[i])
# print(ans)

dp = [inf for _ in range(n)]
ans = 0
for i in range(n):
    dp[bisect_left(dp, a[i])] = a[i]
# print(dp)
print(bisect_left(dp, inf))
