#
# @papamelon app=papamelon.com id=162 lang=python3
#
# [162] 三角形
#
# 枚举O(n**3)
# 排序二分查找 O(n**2*logn)

# @papamelon code=start
from bisect import bisect_left


n = int(input())
a = list(map(int, input().split()))

m = 0

# 书
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             b = a[i] + a[j] + a[k]
#             c = max(a[i], a[j], a[k])
#             d = b - c
#             if d > c:
#                 m = max(m, b)


# better
a.sort()

for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        k = bisect_left(a, s, j + 1) - 1
        if k > j:
            m = max(m, s + a[k])

print(m)
# @papamelon code=end
