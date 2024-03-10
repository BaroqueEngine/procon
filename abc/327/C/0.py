A = [list(map(int, input().split())) for _ in range(9)]


def check(arr):
    return len(set(arr)) == 9


ok = True
for y in range(9):
    if not check(A[y]):
        ok = False

for line in list(zip(*A)):
    if not check(line):
        ok = False

for y in range(3):
    for x in range(3):
        arr = []
        for yy in range(3):
            for xx in range(3):
                tx = x * 3 + xx
                ty = y * 3 + yy
                arr.append(A[ty][tx])
        if not check(arr):
            ok = False

print("Yes" if ok else "No")
