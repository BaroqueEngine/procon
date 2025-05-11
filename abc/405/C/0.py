N = int(input())
A = list(map(int, input().split()))
S = sum(A)

ans = 0
for x in A:
    ans += x * (S - x)
print(ans // 2)