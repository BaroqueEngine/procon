N, M = map(int, input().split())
S = input()
T = input()

ans = []
Q = int(input())
for _ in range(Q):
    W = input()
    takahashi = True
    aoki = True
    for c in W:
        if c not in S:
            takahashi = False
        if c not in T:
            aoki = False
    if takahashi and aoki:
        ans.append("Unknown")
    elif takahashi:
        ans.append("Takahashi")
    else:
        ans.append("Aoki")

for x in ans:
    print(x)