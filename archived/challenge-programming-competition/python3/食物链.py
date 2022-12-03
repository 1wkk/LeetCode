from sys import stdin


input = stdin.readline

n, k = map(int, input().split())

f = [i for i in range(n * 3)]
s = [1 for _ in range(n * 3)]
ans = 0

# n 吃 2 * n, 2 * n 吃 3 * n
def find(x):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]


def union(x, y):
    xx, yy = find(x), find(y)
    if xx == yy:
        return
    if s[xx] > s[yy]:
        xx, yy = yy, xx
    f[xx] = yy
    s[yy] += s[xx]


def pp(x, y):
    return find(x) == find(y)


for i in range(k):
    t, x, y = map(int, input().split())
    # input error
    if x < 1 or x > n or y < 1 or y > n:
        ans += 1
        continue
    # 0 - (n - 1)
    x -= 1
    y -= 1
    if t == 1:
        # t = 1 假设 x，y 同种
        # 如果下述成立则说明 x，y 不是同种
        if pp(x, y + n) or pp(x, y + 2 * n):
            ans += 1
        else:
            union(x, y)
            union(x + n, y + n)
            union(x + 2 * n, y + 2 * n)
    else:
        if pp(x, y) or pp(x, y + 2 * n):
            ans += 1
        else:
            union(x, y + n)
            union(x + n, y + 2 * n)
            union(x + 2 * n, y)
print(ans)
