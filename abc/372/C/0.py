N, Q = map(int, input().split())
S = input()
count = S.count("ABC")
S = list(S)
ans = []

for _ in range(Q):
    X, C = input().split()
    X = int(X)
    X -= 1
    if S[X] != C:
        for start in range(X - 2, X + 1):
            if start >= 0 and S[start:start+3] == list("ABC"):
                count -= 1
        S[X] = C
        for start in range(X - 2, X + 1):
            if start >= 0 and S[start:start+3] == list("ABC"):
                count += 1
    ans.append(count)

for x in ans:
    print(x)
