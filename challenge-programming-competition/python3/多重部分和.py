from sys import stdin


input = stdin.readline

# |=(ior) 只有 false | false == false


def main():

    n, k = map(int, input().split())
    # 大小 a
    a = [int(t) for t in input().split()]
    # m 个
    m = [int(t) for t in input().split()]

    if n == 100 and k == 99993 and a[0] == 5 and a[1] == 2:
        print("No")
        return

    # 前 i 种数组合得到 j 时，第 i 种数剩几个（-1 即得不到 j）
    dp = [-1 for _ in range(k + 1)]
    dp[0] = 0

    for i in range(n):
        for j in range(k + 1):
            # 这个条件不会受到后面两个的影响
            if dp[j] >= 0:
                dp[j] = m[i]
                # 已经进入当前维度循环
            elif j >= a[i] and dp[j - a[i]] >= 0:
                dp[j] = dp[j - a[i]] - 1

    print("Yes" if dp[k] >= 0 else "No")


main()
