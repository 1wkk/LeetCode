#
# @acwing app=acwing.com id=4211 lang=python3
#
# [4211] 序列重排
#
# 回溯

# @acwing code=start


n = int(input())
# 初始化 python 的 bool 数组，使用 v = [False * n] 是错误❌的！！！
# 请使用如下所示方法或 v = [False for i in range(n)]：
v = [False] * n
b = []
a = list(map(int, input().split()))

# print(a)
# print(a)
# print(v)


def dfs():
    if len(b) == n:
        for i in b:
            print(i, end=" ")
        return
    for i in range(n):
        if (not v[i]) and (a[i] == b[-1] * 2 or a[i] * 3 == b[-1]):
            b.append(a[i])
            v[i] = True
            dfs()
            v[i] = False
            b.pop()


for i in range(n):
    b.append(a[i])
    v[i] = True
    dfs()
    v[i] = False
    b.pop()

# @acwing code=end
