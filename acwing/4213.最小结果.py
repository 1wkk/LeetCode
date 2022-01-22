# 爆搜

a = list(map(int, input().split()))
op = input().split()
ans = float("inf")


def dfs(b, u):
    global ans
    if len(b) == 1:
        ans = min(ans, b[0])
    else:
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                n = b[i] + b[j] if op[u] == "+" else b[i] * b[j]
                c = [n]
                for k in range(len(b)):
                    if k != i and k != j:
                        c.append(b[k])
                dfs(c, u + 1)


dfs(a, 0)
print(ans)
