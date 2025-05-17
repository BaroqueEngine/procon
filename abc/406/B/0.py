N, K = map(int, input().split())
A = list(map(int, input().split()))

v = 1
for x in A:
    v *= x
    if len(str(v)) > K:
        v = 1
print(v)