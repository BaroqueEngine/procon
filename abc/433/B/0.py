N = int(input())
A = list(map(int, input().split()))
INF = 10**18

for i in range(N):
    min_value = INF
    min_num = INF
    for j in range(i):
        if A[i] < A[j]:
            min_value = min(min_value, A[j])
            min_num = j + 1
    if min_num == INF:
        min_num = -1
    print(min_num)
