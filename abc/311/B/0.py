N, D = map(int, input().split())
S = [list(input()) for _ in range(N)]

max_cnt = 0
cnt = 0
for line in zip(*S):
    line = "".join(line)
    if line == "o" * N:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        cnt = 0
max_cnt = max(max_cnt, cnt)
print(max_cnt)
