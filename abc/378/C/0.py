N = int(input())
A = list(map(int, input().split()))
B = []

dic = {}

for i in range(N):
    if A[i] in dic:
        B.append(dic[A[i]])
    else:
        B.append(-1)
    dic[A[i]] = i + 1

print(*B)
