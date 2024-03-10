K = int(input())
A = []
for _ in range(K):
    N = int(input())
    A.append(list(map(int, input().split())))
X = int(input())

ans = []
min_size = 10000000000

for i in range(K):
    if X in A[i]:
        size = len(A[i])
        if size < min_size:
            ans = [i + 1]
            min_size = size
        elif size == min_size:
            ans.append(i + 1)

print(len(ans))
print(*ans)
