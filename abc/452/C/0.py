N = int(input())
O = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
S = [input() for _ in range(M)]

MAX = 11
dic = [[[0] * 26 for _ in range(MAX)] for _ in range(MAX)]

def to_i(c):
    return ord(c) - ord("a")

# 肋骨の定義
for text in S:
    l = len(text)
    for i in range(N):
        if len(text) != O[i][0]:
            continue
        c = text[O[i][1] - 1]
        dic[i][l][to_i(c)] += 1

for text in S:
    if len(text) != N:
        print("No")
        continue

    ok = True
    for i, (l, j) in enumerate(O):
        if dic[i][l][to_i(text[i])] == 0:
            ok = False
            break
    print("Yes" if ok else "No")