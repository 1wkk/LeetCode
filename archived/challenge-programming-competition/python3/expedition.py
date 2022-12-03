from heapq import heappop, heappush
from sys import stdin

input = stdin.readline


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    l, p = map(int, input().split())
    a = list(map(lambda x: [l - x[0], x[1]], a))
    a.append([l, 0])
    n += 1
    a.sort()
    # print(a)
    q = []
    ans, cur = 0, 0
    for i in range(n):
        aa, bb = a[i]
        # print("{}, {}".format(aa, bb))
        d = aa - cur
        while p - d < 0:
            if len(q) <= 0:
                print(-1)
                return
            p += -heappop(q)
            ans += 1
        p -= d
        cur = aa
        heappush(q, -bb)
    print(ans)


main()
