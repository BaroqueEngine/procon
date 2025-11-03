import bisect
N, A, B = map(int, input().split())
S = input()

SA = [0]
SB = [0]

for c in S:
    SA.append(SA[-1] + (c == "a"))
    SB.append(SB[-1] + (c == "b"))

ans = 0
for left in range(N):
    right_a = bisect.bisect_left(SA, A + SA[left])
    right_b = bisect.bisect_left(SB, B + SB[left])
    ans += max(0, right_b - right_a)

print(ans)