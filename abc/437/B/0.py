H, W, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
st = set([])
for _ in range(N):
    st.add(int(input()))

for y in range(H):
    for x in range(W):
        if A[y][x] in st:
            A[y][x] = -1

ans = 0
for line in A:
    ans = max(ans, line.count(-1))

print(ans)