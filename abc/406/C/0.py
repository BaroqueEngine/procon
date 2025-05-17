N = int(input())
P = list(map(int, input().split()))
T = []
if P[0] < P[1]:
    T.append(0)
for i in range(1, N - 1):
    if P[i - 1] < P[i] > P[i + 1]:
        T.append(i)
    if P[i - 1] > P[i] < P[i + 1]:
        T.append(i)
T.append(N - 1)

ans = 0
for i in range(0, len(T), 2):
    if i + 3 >= len(T):
        break
    left = T[i + 1] - T[i]
    right = T[i + 3] - T[i + 2]
    ans += left * right

print(ans)