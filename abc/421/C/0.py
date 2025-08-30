N = int(input())
S = input()

A = [i * 2 for i in range(N)]
B = [x + 1 for x in A]
T = []
for i in range(len(S)):
    if S[i] == "A":
        T.append(i)

cnt_a = 0
cnt_b = 0
for i in range(N):
    cnt_a += abs(A[i] - T[i])
    cnt_b += abs(B[i] - T[i])

print(min(cnt_a, cnt_b))