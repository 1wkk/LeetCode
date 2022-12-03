#
# @acwing app=acwing.com id=4210 lang=python3
#
# [4210] 数字
#

# @acwing code=start
A = int(input())
B = A - 2
ans = 0
for i in range(2, A):
    C = A
    while C:
        ans += C % i
        C //= i
for i in range(2, A - 1):
    while ans % i == 0 and B % i == 0:
        ans //= i
        B //= i
print("{}/{}".format(ans, B))
# @acwing code=end
