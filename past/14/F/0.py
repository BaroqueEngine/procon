N = int(input())
base = set(list(map(int, input().split())))
Q = int(input())
ans = []
for _ in range(Q):
    M = int(input())
    common = []
    for x in list(map(int, input().split())):
        if x in base:
            common.append(x)
    ans.append(N + M - len(common))

for x in ans:
    print(x)
