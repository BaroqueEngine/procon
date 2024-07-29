N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

x = 0
y = 0
total_x = 0
total_y = 0
for i in range(N):
    total_x += A[i]
    x += 1
    if total_x > X:
        break
for i in range(N):
    total_y += B[i]
    y += 1
    if total_y > Y:
        break
print(min(x, y))
