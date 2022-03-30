n, x0, y0 = map(int, input().split())
st = set()
c = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y0 - y != 0:
        st.add((x0 - x) / (y0 - y))
    else:
        c = 1
print(len(st) + c)
