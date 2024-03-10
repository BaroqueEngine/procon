N = int(input())

for a in range(N + 1):
    for b in range(N + 1):
        for c in range(N + 1):
            if a + b + c <= N:
                print(a, b, c)
