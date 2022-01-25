from heapq import heappop, heappush
from sys import stdin


n = int(stdin.readline())
l = []
for _ in range(n):
    heappush(l, int(stdin.readline()))
ans = 0
while len(l) > 1:
    p = heappop(l)
    prev = heappop(l)
    c = p + prev
    ans += c
    heappush(l, c)
print(ans)
