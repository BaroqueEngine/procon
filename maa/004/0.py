A = list(map(int, input().split()))
ans = 1
for x in A:
    ans *= x
print(ans)
