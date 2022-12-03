n = int(input())
d = list(map(int, input().split()))
p = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    p[i] = p[i - 1] + d[i - 1]

# double pointer
l, r, ans = 0, n, 0
while l <= r:
    x = p[l]
    y = p[n] - p[r]
    if x == y:
        ans = max(ans, x)
        l += 1
    elif x > y:
        r -= 1
    else:
        l += 1
print(ans)
