#
# @papamelon app=papamelon.com id=193 lang=python3
#
# [193] 蚂蚁
#

# @papamelon code=start
T = int(input())
for _ in range(T):
    L, n = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    mn = max(min(i, L - i) for i in x)
    mx = max(max(i, L - i) for i in x)
    print("{} {}".format(mn, mx))
# @papamelon code=end
