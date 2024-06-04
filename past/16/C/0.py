N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 9
for x in A:
    cnt[x] += 1

print(min(cnt[1:9]))
