N = int(input())
A = list(map(int, input().split()))
seen = set()

for i in range(1, N + 1):
    if i not in seen:
        seen.add(A[i - 1])

ans = []
for i in range(1, N + 1):
    if i not in seen:
        ans.append(i)

print(len(ans))
print(*ans)
