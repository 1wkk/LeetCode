from itertools import combinations


MX = 10 ** 12

fs = [1]

while fs[-1] * (len(fs) + 1) <= MX:
    fs.append(fs[-1] * (len(fs) + 1))

cs = []

# 计算 x的二进制 有多少个 1，即由多少个 2的幂次方 组成
def ct(x):
    cnt = 0
    while x:
        cnt += x & 1
        x >>= 1
    return cnt


# 也可以枚举
for i in range(len(fs) + 1):
    for tp in combinations(fs, i):
        cs.append((sum(tp), len(tp)))

t = int(input())


for _ in range(t):
    n = int(input())
    ans = MX
    for s, c in cs:
        if n - s >= 0:
            ans = min(ans, c + ct(n - s))
    print(ans)
