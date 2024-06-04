N, M = map(int, input().split())

arr = []
for bit in range(2**N):
    line = []
    for i in range(N):
        if bit >> i & 1 == 1:
            line.append(1)
        else:
            line.append(0)
    arr.append(line)

patterns = []
for _ in range(M):
    pattern = []
    k = int(input())
    for _ in range(k):
        pattern.append(list(map(int, input().split())))
    patterns.append(pattern)

for line in arr:
    result = True
    for pattern in patterns:
        ok = False
        for a, b in pattern:
            if line[a - 1] == b:
                ok = True
                break
        if not ok:
            result = False
            break
    if result:
        print("Yes")
        exit()
print("No")
