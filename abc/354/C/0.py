
N = int(input())
A = [list(map(int, input().split())) + [i] for i in range(1, N + 1)]
A.sort()

ans = [A[-1][2]]
min_c = A[-1][1]
for i in range(N - 2, -1, -1):
    a, c, index = A[i]
    if c < min_c:
        ans.append(index)
        min_c = c

ans.sort()
print(len(ans))
print(*ans)
