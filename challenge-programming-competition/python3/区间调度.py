import functools


def cmp(a, b):
    _, e1 = a
    _, e2 = b
    return e1 - e2


while True:
    try:
        n = int(input())
        t = []
        for _ in range(n):
            s, e = map(int, input().split())
            t.append((s, e))
        t.sort(key=functools.cmp_to_key(cmp))
        # print(t)
        ans, c = 0, 0
        for s, e in t:
            if c < s:
                c = e
                ans += 1
        print(ans)
    except EOFError:
        break
