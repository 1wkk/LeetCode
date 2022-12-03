n, t = map(int, input().split())
p = list(map(int, input().split()))
c = [[] for _ in range(n + 1)]
for ch, f in enumerate(p):
    c[f].append(ch + 2)
sz = [0 for _ in range(n + 1)]
q = []
p = [0 for _ in range(n + 10)]


def dfs(u):
    sz[u] = 1
    q.append(u)
    p[u] = len(q) - 1
    for v in c[u]:
        dfs(v)
        sz[u] += sz[v]


dfs(1)

for _ in range(t):
    u, k = map(int, input().split())
    if k > sz[u]:
        print(-1)
    else:
        print(q[p[u] + k - 1])
