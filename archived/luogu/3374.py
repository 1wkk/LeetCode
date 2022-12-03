n, m = map(int, input().split())
f = [0] * (4 * 5 * (10 ** 5))
a = list(map(int, input().split()))


def build(k, l, r):
    if l == r:
        f[k] = a[l - 1]
        return
    mid = (l + r) >> 1
    build(2 * k, l, mid)
    build(2 * k + 1, mid + 1, r)
    f[k] = f[2 * k] + f[2 * k + 1]


build(1, 1, n)


def add(k, l, r, x, y):
    f[k] += y
    if l == r:
        return
    mid = (l + r) >> 1
    if x <= mid:
        add(2 * k, l, mid, x, y)
    else:
        add(2 * k + 1, mid + 1, r, x, y)


def _sum(k, l, r, x, y):
    if l == x and r == y:
        return f[k]
    mid = (l + r) >> 1
    if y <= mid:
        return _sum(2 * k, l, mid, x, y)
    else:
        if x > mid:
            return _sum(2 * k + 1, mid + 1, r, x, y)
        else:
            return _sum(2 * k, l, mid, x, mid) + _sum(2 * k + 1, mid + 1, r, mid + 1, y)


for _ in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        add(1, 1, n, x, y)
    else:
        print(_sum(1, 1, n, x, y))
