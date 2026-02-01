N, T = map(int, input().split())
A = list(map(int, input().split())) + [T]

ans = 0
cur_time = 0
open_time = 0
for x in A:
    cur_time = open_time
    ans += max(0, x - cur_time)
    if x >= open_time:
        open_time = x + 100

print(ans)