N = int(input())
A = list(map(int, input().split()))
dic = {}
for j in range(N):
    v = (j + 1) - A[j]
    dic[v] = dic.get(v, 0) + 1

ans = 0
for i in range(N):
    v = (i + 1) - A[i]
    if v in dic:
        dic[v] -= 1
    ans += dic.get((i + 1) + A[i], 0)

print(ans)