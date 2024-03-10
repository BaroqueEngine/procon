import itertools
S = [list(map(int, input().split())) for _ in range(3)]

P = [0, 1, 2, 3, 4, 5, 6, 7, 8]
success = 362880
all = 362880


def index_to_xy(index):
    return (index % 3, index // 3)


def check_row(A, x, y):
    row = []
    for tx in range(3):
        row.append(A[y][tx])

    if -1 in row:
        return True

    row.pop(x)

    return row[0] != row[1]


def check_col(A, x, y):
    col = []
    for ty in range(3):
        col.append(A[ty][x])

    if -1 in col:
        return True

    col.pop(y)

    return col[0] != col[1]


def check_naname_0(A, index):
    if index not in [0, 4, 8]:
        return True

    dic = {
        0: 0,
        4: 1,
        8: 2
    }

    naname = []
    for i in range(3):
        naname.append(A[i][i])

    if -1 in naname:
        return True

    naname.pop(dic[index])

    return naname[0] != naname[1]


def check_naname_1(A, index):
    if index not in [2, 4, 6]:
        return True

    dic = {
        2: 0,
        4: 1,
        6: 2
    }

    naname = []
    for i in range(3):
        naname.append(A[i][2 - i])

    if -1 in naname:
        return True

    naname.pop(dic[index])

    return naname[0] != naname[1]


for v in itertools.permutations(P):
    A = [[-1] * 3 for _ in range(3)]

    ok = True
    for index in v:
        x, y = index_to_xy(index)
        A[y][x] = S[y][x]

        if not check_row(A, x, y):
            ok = False
            break

        if not check_col(A, x, y):
            ok = False
            break

        if not check_naname_0(A, index):
            ok = False
            break

        if not check_naname_1(A, index):
            ok = False
            break

    if not ok:
        success -= 1

print(success / all)
