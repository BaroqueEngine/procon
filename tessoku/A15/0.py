N = int(input())
A = list(map(int, input().split()))
B = sorted(list(set(A)))

dic = {}
for i in range(len(B)):
    dic[B[i]] = i + 1

ans = []
for x in A:
    ans.append(dic[x])
print(*ans)