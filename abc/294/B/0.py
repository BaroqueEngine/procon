H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for line in A:
    s = ""
    for x in line:
        if x == 0:
            s += "."
        else:
            s += chr(ord("A") + x - 1)
    print(s)
