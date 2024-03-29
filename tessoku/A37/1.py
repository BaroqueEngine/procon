N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
ans += sum(A) * M
ans += B * (N * M)
ans += sum(C) * N
print(ans)