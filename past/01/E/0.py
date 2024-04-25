N, Q = map(int, input().split())
A = [[False] * N for _ in range(N)]
for _ in range(Q):
    T = list(map(int, input().split()))
    if T[0] == 1:
        x, y = T[1:]
        x -= 1
        y -= 1
        A[x][y] = True
    elif T[0] == 2:
        x = T[1]
        x -= 1
        for i in range(N):
            if x == i:
                continue
            if A[i][x]:
                A[x][i] = True
    else:
        x = T[1]
        x -= 1
        friends = []
        for i in range(N):
            if A[x][i]:
                friends.append(i)
        friends2 = set()
        for y in friends:
            for z in range(N):
                if z == x:
                    continue
                if A[y][z]:
                    friends2.add(z)
        for y in friends2:
            A[x][y] = True

for y in range(N):
    line = A[y]
    s_line = "".join(["Y" if x else "N" for x in line])
    print(s_line)
