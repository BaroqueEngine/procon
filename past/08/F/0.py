from collections import deque

N = int(input())
S = input()

zero_pos = deque([])
for i in range(N):
    if S[i] == "0":
        zero_pos.append(i + 1)

if len(zero_pos) == 1:
    print(-1)
    exit()

if len(zero_pos) >= 2:
    zero_pos.append(zero_pos.popleft())

ans = []
for i in range(N):
    if S[i] == "1":
        ans.append(i + 1)
    else:
        ans.append(zero_pos.popleft())
print(*ans)