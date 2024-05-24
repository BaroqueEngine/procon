from collections import deque
R, N, M, L = map(int, input().split())
S = deque(list(map(int, input().split())))

for _ in range(R):
    rest = N
    for _ in range(M):
        if len(S) == 0:
            print("No")
            exit()
        rest -= S.popleft()
        if rest < 0:
            print("No")
            exit()
        if rest == 0:
            break

if len(S) != 0:
    print("No")
    exit()
print("Yes")