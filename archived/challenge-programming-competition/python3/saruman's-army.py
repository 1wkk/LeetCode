while True:
    r, n = map(int, input().split())
    if r == -1 and n == -1:
        break
    x = [*map(int, input().split())]
    x.sort()
    ans, idx = 0, 0
    while idx < n:
        s, idx = x[idx], idx + 1
        while idx < n and x[idx] <= s + r:
            idx += 1
        p = x[idx - 1]
        while idx < n and x[idx] <= p + r:
            idx += 1
        ans += 1
    print(ans)
