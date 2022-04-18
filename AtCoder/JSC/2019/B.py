n, k = map(int, input().split())
a = list(map(int, input().split()))
M = 10 ** 9 + 7
ans = 0

for i, v in enumerate(a):
    c = 0
    cc = 0
    for vv in a[i + 1 :]:
        if vv < v:
            c += 1
    for vv in a:
        if vv < v:
            cc += 1
    ans += ((c + (c + cc * (k - 1))) * k // 2) % M
print(ans % M)
