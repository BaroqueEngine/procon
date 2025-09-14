N, start = map(int, input().split())
D = list(map(int, input().split()))
S = [0]
for x in D:
    S.append(S[-1] + x)

if S[-1] == N:
    print(0)
    exit()

left = N - 1
right = 0

for i in range(N):
    if D[i] == 0:
        left = min(left, i)
        right = max(right, i)

left = min(left, start)
right = max(right, start - 1)

ans = right - left + 1
ans += S[right + 1] - S[left]
print(ans)