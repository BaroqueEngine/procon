N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
S = list(set(A))

cur = 0
for i in range(min(K, len(S))):
    x = S[i]
    if cur == x:
        cur += 1
    else:
        break
print(cur)
