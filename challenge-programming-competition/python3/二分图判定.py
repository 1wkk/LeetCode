from collections import defaultdict


def main():
    while True:
        try:
            n = int(input())
            e = defaultdict(list)
            c = [0 for _ in range(n)]

            def dfs(v, cc):
                c[v] = cc
                for vv in e[v]:
                    if c[vv] == c:
                        return False
                    elif c[vv] == 0 and not dfs(vv, -cc):
                        return False
                return True

            for _ in range(n):
                u, v = map(int, input().split())
                e[u].append(v)
                e[v].append(u)

            for i in range(n):
                if c[i] == 0:
                    if not dfs(i, 1):
                        print("No")
                        return
            print("Yes")
        except EOFError:
            break


main()
