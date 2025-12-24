N = int(input())
A = list(map(int, input().split()))
ans = 0

for l in range(N):
    for r in range(l, N):
        total = sum(A[l : r + 1])
        ok = True
        for i in range(l, r + 1):
            if total % A[i] == 0:
                ok = False
                break
        if ok:
            ans += 1

print(ans)