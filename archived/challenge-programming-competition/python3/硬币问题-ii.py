t = int(input())

coins = [1, 5, 10, 50, 100, 500]

for _ in range(t):
    c = [*map(int, input().split())]
    a = int(input())
    ans = 0
    for i in range(5, -1, -1):
        # print(a, end=", ")
        n = min(a // coins[i], c[i])
        # print("{}, {}".format(i, n))
        a -= n * coins[i]
        ans += n
    print(ans)
