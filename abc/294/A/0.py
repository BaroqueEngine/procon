N = int(input())
A = list(map(int, input().split()))

ans = []

for x in A:
    if x % 2 == 0:
        ans.append(x)

print(*ans)
