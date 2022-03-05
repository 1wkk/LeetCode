from collections import Counter


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_counter = Counter(a)
for x in b:
    if a_counter[x]:
        a_counter[x] -= 1
    else:
        print('No')
        break
else:
    print('Yes')
