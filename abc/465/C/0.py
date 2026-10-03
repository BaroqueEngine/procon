from collections import deque

N = int(input())
S = input()

ans = deque([1])
is_suffix = False

for i in range(1, N):
    if is_suffix:
        ans.appendleft(i + 1)
    else:
        ans.append(i + 1)
    if S[i] == "o":
        is_suffix = not is_suffix

if is_suffix:
    ans.reverse()

print(*[x for x in ans])