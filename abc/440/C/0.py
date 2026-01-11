def solve():
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    SIZE = 2 * W
    A = [0] * SIZE
    for i in range(N):
        A[i % SIZE] += C[i]
    min_cost = cost = sum(A[: W])
    for i in range(SIZE):
        cost -= A[i]
        cost += A[(i + W) % SIZE]
        min_cost = min(min_cost, cost)

    return min_cost

ans = []
T = int(input())
for _ in range(T):
    ans.append(solve())

for x in ans:
    print(x)