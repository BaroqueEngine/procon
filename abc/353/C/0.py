N = int(input())
A = list(map(int, input().split()))
MOD = 10**8
total = sum(A) * (N - 1)
A.sort()
j = N - 1
for i in range(N - 1):
    j = max(j, i + 1)
    if i == j:
        break
    while i < j and (A[i] + A[j]) >= MOD:
        j -= 1
    over_cnt = N - 1 - j
    total -= MOD * over_cnt
print(total)
