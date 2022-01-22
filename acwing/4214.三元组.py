n = int(input())
s = list(map(int, input().split()))
c = list(map(int, input().split()))

mx = float("inf")

for j in range(n):
    l = float("inf")
    r = float("inf")
    for i in range(j):
        if s[i] < s[j]:
            l = min(l, c[i])
    for k in range(j + 1, n):
        if s[k] > s[j]:
            r = min(r, c[k])
    mx = min(mx, l + c[j] + r)

print(-1 if mx == float("inf") else mx)
