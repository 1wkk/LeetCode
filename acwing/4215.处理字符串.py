# from sys import stdin


# input = stdin.readline

s = input()

a = ""

for ss in s:
    c = ss.lower()
    if ss not in ["a", "o", "y", "e", "u", "i"]:
        a += "." + c

print(a)
