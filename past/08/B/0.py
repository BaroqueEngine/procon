N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

ans = []
for a in A:
    if a in B:
        ans.append(a)
print(*ans)