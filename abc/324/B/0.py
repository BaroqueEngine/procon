N = int(input())

if N == 1:
    print("Yes")
    exit()

x = 0
while N % 2 == 0:
    N //= 2
    x += 1

y = 0
while N % 3 == 0:
    N //= 3
    y += 1

if N != 1:
    print("No")
    exit()

if x == 0 and y == 0:
    print("No")
    exit()

print("Yes")
