from sortedcontainers import SortedList


a = SortedList()

n = int(input())
for _ in range(n):
    ipt = input().split()
    if len(ipt) == 2:
        flag, x = map(int, ipt)
        a.add(x)
    else:
        flag, x, k = map(int, ipt)
        if flag == 2:
            idx = a.bisect_right(x)
            if idx < k:
                print(-1)
            else:
                print(a[idx - k])
        else:
            idx = a.bisect_left(x)
            if len(a) - idx < k:
                print(-1)
            else:
                print(a[idx - 1 + k])
