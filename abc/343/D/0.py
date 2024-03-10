from collections import defaultdict

N, T = map(int, input().split())
members = [0] * (N + 1)
score = defaultdict(int)
score[0] = N
ans = 1
for _ in range(T):
    A, B = map(int, input().split())
    score[members[A]] -= 1
    if score[members[A]] == 0:
        ans -= 1
    members[A] += B
    score[members[A]] += 1
    if score[members[A]] == 1:
        ans += 1
    print(ans)
