S, A, B, X = map(int, input().split())

ans = 0
cnt = X // (A + B)
ans += A * cnt
X -= (A + B) * cnt
X = min(X, A)
ans += X
ans *= S
print(ans)