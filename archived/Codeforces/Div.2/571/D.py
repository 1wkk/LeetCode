from math import floor

n = int(input())
a = [0 for _ in range(n)]
s = 0
for i in range(n):
    v = float(input())
    a[i] = v
    s += floor(v)

for v in a:
    if s < 0 and v != floor(v):
        s += 1
        print(floor(v) + 1)
    else:
        print(floor(v))
