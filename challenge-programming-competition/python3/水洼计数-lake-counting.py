#
# @papamelon app=papamelon.com id=202 lang=python3
#
# [202] 水洼计数 Lake Counting
#

# @papamelon code=start
from sys import setrecursionlimit


setrecursionlimit(10000)

n, m = map(int, input().split())
w = []
for _ in range(n):
    s = input()
    w.append([s[i] for i in range(m)])


def dfs(x, y):
    # print(w)
    w[x][y] = "."
    for i in range(-1, 2):
        for j in range(-1, 2):
            nx, ny = i + x, j + y
            if nx >= 0 and nx < n and ny >= 0 and ny < m and w[nx][ny] == "W":
                dfs(nx, ny)


ans = 0
# print(w)
for i in range(n):
    for j in range(m):
        if w[i][j] == "W":
            ans += 1
            dfs(i, j)
print(ans)
# @papamelon code=end
