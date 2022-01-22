#
# @papamelon app=papamelon.com id=194 lang=python3
#
# [194] 抽签
#

# @papamelon code=start
n = int(input())
m = int(input())
k = list(map(int, input().split()))
f = False

for a in k:
    for b in k:
        for c in k:
            for d in k:
                if a + b + c + d == m:
                    f = True
print("Yes") if f else print("No")
# @papamelon code=end
