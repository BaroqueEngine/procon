N, M = map(int, input().split())
A = list(map(int, input().split()))
unsolved = [[] for _ in range(N)]
score = [0] * N

for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == "o":
            score[i] += A[j]
        else:
            unsolved[i].append(A[j])
    score[i] += (i + 1)
    unsolved[i].sort()

target_score = max(score)

for i in range(N):
    ans = 0
    while score[i] < target_score:
        score[i] += unsolved[i].pop()
        ans += 1
    print(ans)
