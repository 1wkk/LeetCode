#
# @papamelon app=papamelon.com id=203 lang=python3
#
# [203] 迷宫的最短路径
#

# @papamelon code=start
from cmath import inf
from collections import deque


n, m = map(int, input().split())
f = []
for _ in range(n):
    f.append(input())
sx, sy, ex, ey = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if f[i][j] == "S":
            sx, sy = i, j
        if f[i][j] == "G":
            ex, ey = i, j
q = deque()
q.append((sx, sy))
d = [[inf for _ in range(m)] for _ in range(n)]
r = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d[sx][sy] = 0
while q:
    x, y = q.popleft()
    if x == ex and y == ey:
        break
    for rr in r:
        xx, yy = rr
        # print((xx, yy))
        nx, ny = x + xx, y + yy
        if (
            nx >= 0
            and ny >= 0
            and nx < n
            and ny < m
            and f[nx][ny] != "#"
            and d[nx][ny] == inf
        ):
            q.append((nx, ny))
            d[nx][ny] = d[x][y] + 1
# 必定有解
print(d[ex][ey])
# @papamelon code=end
