N = int(input())

print(N)
for i in range(1, N + 1):
    u = i
    v = i + 1
    if v > N:
        v = 1
    print("{} {}".format(u, v))