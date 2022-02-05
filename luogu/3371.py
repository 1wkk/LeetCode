from collections import defaultdict
from heapq import heappop, heappush
from sys import stdin

input = stdin.readline

e = defaultdict(list)

n, m, s = map(int, input().split())
inf = 2 ** 31 - 1
dis = [inf for _ in range(n + 1)]
vis = [False for _ in range(n + 1)]
q = [(0, s)]

for _ in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, w))

dis[s] = 0

while q:
    _, u = heappop(q)
    if not vis[u]:
        vis[u] = True
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                if not vis[v]:
                    heappush(q, (dis[v], v))


print(*dis[1:])
