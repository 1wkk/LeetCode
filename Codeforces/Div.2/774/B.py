t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ls, rs = a[0], 0
    l, r = 1, len(a) - 1
    while l < r:
        ls, rs = ls + a[l], rs + a[r]
        l, r = l + 1, r - 1
        if rs > ls:
            print('YES')
            break
    else:
        print('NO')
