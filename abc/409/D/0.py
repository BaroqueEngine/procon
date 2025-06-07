T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    if N <= 2:
        ans.append("".join(sorted(S)))
        continue
    l = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            l = i
            break
    if l == -1:
        ans.append(S)
        continue
    r = N
    for j in range(l + 2, N):
        if S[l] < S[j]:
            r = j
            break
    ans.append(S[:l] + S[l + 1:r] + S[l] + S[r:])

for x in ans:
    print(x)
            