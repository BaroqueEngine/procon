N = int(input())
P = list(map(int, input().split()))
Q = int(input())

ans = []
for _ in range(Q):
    A, B = map(int, input().split())
    if P.index(A) < P.index(B):
        ans.append(A)
    else:
        ans.append(B)

for x in ans:
    print(x)
