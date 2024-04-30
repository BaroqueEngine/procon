from collections import Counter

N, M, K = map(int, input().split())
S = [input() for _ in range(N)]
ans = 1
for n in range(2, min(N, M) + 1):
    for y in range(N - n + 1):
        for x in range(M - n + 1):
            arr = []
            for ty in range(y, y + n):
                for tx in range(x, x + n):
                    arr.append(int(S[ty][tx]))
            counter = Counter(arr)
            num = counter.most_common()[0][1]
            if n * n - num <= K:
                ans = n
print(ans)