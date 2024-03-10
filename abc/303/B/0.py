N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

s = set()
for i in range(N):
    for j in range(i + 1, N):
        s.add((i + 1, j + 1))

for line in A:
    for i in range(N - 1):
        a = line[i]
        b = line[i + 1]

        if b < a:
            a, b = b, a

        if (a, b) in s:
            s.remove((a, b))

print(len(s))