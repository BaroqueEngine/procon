N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
SC = sum(C)

ans = B * N * M
for a in A:
    ans += a * M + SC
print(ans)
