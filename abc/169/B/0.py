N = int(input())
A = list(map(int, input().split()))

ans = 1
for x in A:
    ans = min(ans * x, 10**18+1)

if ans == 10**18+1:
    ans = -1
print(ans)
