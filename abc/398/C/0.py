N = int(input())
A = list(map(int, input().split()))
dic = {}
for x in A:
    dic[x] = dic.get(x, 0) + 1

max_v = -1
for i in range(N):
    if dic[A[i]] == 1:
        max_v = max(max_v, A[i])

if max_v == -1:
    print(-1)
else:
    print(A.index(max_v) + 1)