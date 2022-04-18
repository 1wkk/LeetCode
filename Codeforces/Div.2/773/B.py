t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    st = set(a)
    ans = []
    for i in range(n):
        if i + 1 <= len(st):
            ans.append(str(len(st)))
        else:
            ans.append(str(i + 1))
    print(' '.join(ans))
