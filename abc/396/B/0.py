Q = int(input())
A = [0] * 100
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        A.append(x)
    else:
        ans.append(A.pop())

for x in ans:
    print(x)