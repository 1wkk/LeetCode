n = int(input())
s = []
for _ in range(n):
    s.append(input())
l, r = 0, n - 1
t = []
while l <= r:
    flag = False
    ll, rr = l, r
    while ll <= rr:
        if s[ll] < s[rr]:
            flag = True
            break
        elif s[ll] > s[rr]:
            flag = False
            break
        ll += 1
        rr -= 1
    if flag:
        t.append(s[l])
        l += 1
    else:
        t.append(s[r])
        r -= 1
idx = 1
for c in t:
    print(c, end="" if idx % 80 != 0 else "\n")
    idx += 1
