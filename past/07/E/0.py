N = int(input())

for a in range(30):
    x = 1
    for b in range(30):
        x *= 3
        if a == b:
            x += 1
    if x == N:
        print(a + 1)
        exit()
print(-1)
