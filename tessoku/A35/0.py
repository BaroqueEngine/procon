N = int(input())
A = list(map(int, input().split()))

score = A[:]
for i in range(N - 2, -1, -1):
    # first
    for j in range(i + 1):
        if i % 2 == 0:
            score[j] = max(score[j], score[j + 1])
        else:
            score[j] = min(score[j], score[j + 1])
    score.pop()

print(score[0])