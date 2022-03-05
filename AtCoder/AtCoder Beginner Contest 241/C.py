# input
n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))


def slove():
    for i in range(n):
        for j in range(n):
            if i + 5 < n:
                cnt = 0
                for k in range(6):
                    if grid[i + k][j] == '.':
                        cnt += 1
                if cnt <= 2:
                    print('Yes')
                    return
            if j + 5 < n:
                cnt = 0
                for k in range(6):
                    if grid[i][j + k] == '.':
                        cnt += 1
                if cnt <= 2:
                    print('Yes')
                    return
            if i + 5 < n and j + 5 < n:
                cnt = 0
                for k in range(6):
                    if grid[i + k][j + k] == '.':
                        cnt += 1
                if cnt <= 2:
                    print('Yes')
                    return
            if i + 5 < n and j - 5 >= 0:
                cnt = 0
                for k in range(6):
                    if grid[i + k][j - k] == '.':
                        cnt += 1
                if cnt <= 2:
                    print('Yes')
                    return

    print('No')


slove()
