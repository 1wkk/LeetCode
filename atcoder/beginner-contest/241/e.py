n, k = map(int, input().split())
a = list(map(int, input().split()))
x = 0
for _ in range(k):
    x += a[x % n]
print(x)
# TODO
