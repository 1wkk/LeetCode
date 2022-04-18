s = input()
n = len(s)
ss = [0 for _ in range(n)]

pre = -1
for i in range(n):
    if s[i] == 'R':
        pre = i
    else:
        if (i - pre) % 2 == 0:
            ss[pre] += 1
        else:
            ss[pre + 1] += 1
pre = -1
for i in range(n - 1, -1, -1):
    if s[i] == 'L':
        pre = i
    else:
        if (pre - i) % 2 == 0:
            ss[pre] += 1
        else:
            ss[pre - 1] += 1
print(*ss)
