def solve():
    N, H = map(int, input().split())
    min_pos = max_pos = H
    prev_time = 0
    ok = True

    for _ in range(N):
        T, L, U = map(int, input().split())
        diff_time = T - prev_time
        max_pos += diff_time
        min_pos -= diff_time

        if U < min_pos or max_pos < L:
            ok = False
        max_pos = min(max_pos, U)
        min_pos = max(min_pos, L)
        prev_time = T

    return "Yes" if ok else "No"

ans = []
T = int(input())
for _ in range(T):
    ans.append(solve())

for x in ans:
    print(x)