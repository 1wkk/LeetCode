from collections import defaultdict


n, m = map(int, input().split())
e = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    e[a].append(b)
    e[b].append(a)

v = [False for _ in range(n + 1)]


def dfs(x):
    v[x] = True
    for xx in e[x]:
        if not v[xx]:
            dfs(xx)


dfs(1)
if n == m:
    dfs(1)
    if v.count(True) == n:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
