T = int(input())
ans = []

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)

    cnt = 0
    j = 0

    for i in range(N):
        if A[i] + B[j] >= M:
            cnt += 1
            j += 1

    ans.append(sum(A) + sum(B) - cnt * M)

for _ in range(T):
    solve()

for x in ans:
    print(x)