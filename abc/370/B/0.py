N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

cur = 0

for i in range(N):
    cur = A[cur][i] if cur >= i else A[i][cur]
    cur -= 1
print(cur + 1)
