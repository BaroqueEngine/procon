A = []
Q = int(input())
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        A.append(x)
    else:
        print(A[-x])
