t = input()
r = input().split()
a = 0
for i in range(len(r)):
    if r[i] == t:
        a += 1
print(a)
