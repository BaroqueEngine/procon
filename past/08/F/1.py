from collections import deque

N = int(input())
S = input()

zero_pos = deque([])
for i in range(N):
    if S[i] == "0":
        zero_pos.append(i + 1)

if len(zero_pos) == 0:
    ans = []
    for i in range(1, N + 1):
        ans.append(i)
    print(*ans)
    exit()

if len(zero_pos) == 1:
    print(-1)
    exit()

zero_index = 1
ans = []
for i in range(N):
    if S[i] == "1":
        ans.append(i + 1)
    else:
        ans.append(zero_pos[zero_index])
        zero_index = (zero_index + 1) % len(zero_pos)
print(*ans)