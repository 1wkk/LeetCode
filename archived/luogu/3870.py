from math import sqrt

MAX_N = 10 ** 5 + 5
b = [0 for _ in range(MAX_N)]
a = [0 for _ in range(MAX_N)]
on = [0 for _ in range(MAX_N)]
s = [0 for _ in range(MAX_N)]

n, m = map(int, input().split())


block = int(sqrt(n))
for i in range(1, n + 1):
    b[i] = (i - 1) // block + 1


def update(l, r):
    for i in range(l, min(r, (b[l]) * block) + 1):
        s[b[i]] -= a[i] ^ on[b[i]]
        a[i] ^= 1
        s[b[i]] += a[i] ^ on[b[i]]
    if b[l] != b[r]:
        for i in range((b[r] - 1) * block + 1, r + 1):
            s[b[i]] -= a[i] ^ on[b[i]]
            a[i] ^= 1
            s[b[i]] += a[i] ^ on[b[i]]
    for i in range(b[l] + 1, b[r]):
        on[i] ^= 1
        s[i] = block - s[i]


def query(l, r):
    ans = 0
    for i in range(l, min(r, (b[l]) * block) + 1):
        ans += a[i] ^ on[b[i]]
    if b[l] != b[r]:
        for i in range((b[r] - 1) * block + 1, r + 1):
            ans += a[i] ^ on[b[i]]
    for i in range(b[l] + 1, b[r]):
        ans += s[i]
    print(ans)


for _ in range(m):
    c, l, r = map(int, input().split())
    if c:
        query(l, r)
    else:
        update(l, r)
