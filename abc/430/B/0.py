N, M = map(int, input().split())
S = [input() for _ in range(N)]

st = set([])

for y in range(N - M + 1):
    for x in range(N - M + 1):
        cells = ""
        for ty in range(y, y + M):
            cells += S[ty][x:x+M]
        st.add(cells)

print(len(st))