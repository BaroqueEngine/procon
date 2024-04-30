N = int(input())
row = [None] + [x for x in range(1, N + 1)]
col = [None] + [x for x in range(1, N + 1)]
rev = False

ans = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if rev:
        if query[0] == 1:
            query[0] = 2
        elif query[0] == 2:
            query[0] = 1

    if query[0] == 1:
        A, B = query[1:]
        row[A], row[B] = row[B], row[A]
    elif query[0] == 2:
        A, B = query[1:]
        col[A], col[B] = col[B], col[A]
    elif query[0] == 3:
        rev = not rev
    else:
        A, B = query[1:]
        if rev:
            A, B = B, A
        A = row[A]
        B = col[B]
        ans.append(N * (A - 1) + B - 1)

for x in ans:
    print(x)
