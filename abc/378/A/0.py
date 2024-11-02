A = list(map(int, input().split()))
A.sort()

ans = 0
while len(A) >= 2:
    if A[-1] == A[-2]:
        ans += 1
        A.pop()
        A.pop()
    else:
        A.pop()

print(ans)
