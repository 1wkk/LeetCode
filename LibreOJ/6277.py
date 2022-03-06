# Python can not pass.
from math import sqrt


n = int(input())
ipt = list(map(int, input().split()))

MAX_N = 50005
a = [0 for _ in range(MAX_N)]
b = [0 for _ in range(MAX_N)]
v = [0 for _ in range(MAX_N)]


# build
block = int(sqrt(n))
for i in range(1, n + 1):
    b[i] = (i - 1) // block + 1


def query(r):
    print(a[r] + v[b[r]])


def update(l, r, c):
    for i in range(l, min(r, b[l] * block) + 1):
        a[i] += c
    if b[l] != b[r]:
        for i in range((b[r] - 1) * block + 1, r + 1):
            a[i] += c
    for i in range(b[l] + 1, b[r] - 1 + 1):
        v[i] += c


for i in range(1, n + 1):
    a[i] = ipt[i - 1]
for _ in range(n):
    opt, l, r, c = map(int, input().split())
    if opt:
        query(r)
    else:
        update(l, r, c)
