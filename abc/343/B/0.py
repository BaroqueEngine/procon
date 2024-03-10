N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if A[i] == 1:
            ans.append(i + 1)
    print(*ans)
