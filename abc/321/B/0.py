N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(101):
    B = [i] + A[:]
    B.sort()
    B = B[1:-1]
    if sum(B) >= X:
        print(i)
        exit()
print(-1)
