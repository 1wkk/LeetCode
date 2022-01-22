#
# @papamelon app=papamelon.com id=201 lang=python3
#
# [201] 部分和问题
#

# @papamelon code=start

n, a, k = 0, [], 0


def dfs(i, sum):
    if i == n:
        return sum == k
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + a[i]):
        return True
    return False


while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        k = int(input())
        print("Yes") if dfs(0, 0) else print("No")
    except EOFError:
        break

# @papamelon code=end
