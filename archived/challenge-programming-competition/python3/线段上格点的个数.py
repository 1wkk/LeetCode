from sys import stdin


input = stdin.readline

x1, y1, x2, y2 = map(int, input().split())


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


xx = abs(x1 - x2)
yy = abs(y1 - y2)

print((gcd(xx, yy) - 1) if xx != 0 and yy != 0 else 0)
