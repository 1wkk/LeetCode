#
# @acwing app=acwing.com id=4209 lang=python3
#
# [4209] 三元组
#

# @acwing code=start
n = int(input())
a, b, c = 0, 0, 0
for _ in range(n):
    aa, bb, cc = map(int, input().split())
    a, b, c = a + aa, b + bb, c + cc
print("YES" if a == 0 and b == 0 and c == 0 else "NO")
# @acwing code=end
