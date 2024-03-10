N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

dic = {}
for i in range(M):
    dic[D[i]] = P[i + 1]

ans = 0
for c in C:
    if c in dic:
        ans += dic[c]
    else:
        ans += P[0]
print(ans)
