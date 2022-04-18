t = int(input())
for _ in range(t):
    vs = []
    for _ in range(3):
        x, y = map(int, input().split())
        vs.append((y, x))
    vs.sort()
    if vs[1][0] == vs[2][0]:
        print(float(abs(vs[1][1] - vs[2][1])))
    else:
        print(float(0))
