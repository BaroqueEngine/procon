import itertools

H, W = map(int, input().split())
ans = []
for _ in range(H):
    S = input()
    ans.append(S.replace("TT", "PC"))

for line in ans:
    print(line)
