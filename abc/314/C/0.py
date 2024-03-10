N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

max_c = max(C)
dic = [[] for _ in range(max_c + 1)]
pos = [[] for _ in range(max_c + 1)]

for i in range(N):
    dic[C[i]].append(S[i])
    pos[C[i]].append(i)

ans = [""] * N

for i in range(1, max_c + 1):
    if len(dic[i]) == 0:
        continue
    first = pos[i].pop(0)
    pos[i].append(first)
    for j in range(len(pos[i])):
        ans[pos[i][j]] = dic[i][j]

print("".join(ans))
