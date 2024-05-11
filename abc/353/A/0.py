N = int(input())
H = [None] + list(map(int, input().split()))

base = H[1]
for i in range(2, N + 1):
    if base < H[i]:
        print(i)
        exit()
print(-1)
