n = int(input())
a = int(input())
b = int(input())


def main():
    x = 0
    while a * x <= n:
        if (n - a * x) % b == 0:
            print('YES')
            print('{} {}'.format(x, (n - a * x) // b))
            return
        x += 1
    print('NO')


main()
