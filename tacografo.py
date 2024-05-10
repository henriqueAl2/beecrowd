n = int(input())
dt = 0
for i in range (n):
    t, vm = input().split()
    vm = int(vm)
    t = int(t)
    dt = dt +(vm*t)
print(dt)