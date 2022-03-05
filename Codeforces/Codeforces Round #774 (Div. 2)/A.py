t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    n2 = n ** 2
    print(s // n2)
