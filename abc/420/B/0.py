N, M = map(int, input().split())
S = [list(map(int, list(input()))) for _ in range(N)]

scores = [0] * N
for i in range(M):
    vote = [0] * 2
    for j in range(N):
        vote[S[j][i]] += 1
    cur_score = [vote[0] < vote[1], vote[1] < vote[0]]
    for j in range(N):
        scores[j] += cur_score[S[j][i]]

max_score = max(scores)
ans = []
for i in range(N):
    if scores[i] == max_score:
        ans.append(i + 1)

print(*ans)