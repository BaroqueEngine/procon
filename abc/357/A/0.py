N, M = map(int, input().split())
H = list(map(int, input().split()))
for i in range(N):
    if H[i] > M:
        print(i)
        exit()
    M -= H[i]
print(N)
