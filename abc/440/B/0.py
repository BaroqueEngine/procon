N = int(input())
T = list(map(int, input().split()))
A = []
for i in range(N):
    A.append((T[i], i + 1))
A.sort()

ans = []
for x, i in A[:3]:
    ans.append(i)
print(*ans)