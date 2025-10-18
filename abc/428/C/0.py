Q = int(input())
ans = []
depth = 0
C = []
bad_index = -1
for i in range(Q):
    T = input().split()
    if T[0] == "1":
        C.append(T[1])
        if C[-1] == "(":
            depth += 1
        else:
            depth -= 1
    else:
        if C[-1] == "(":
            depth -= 1
        else:
            depth += 1
        C.pop()
        if bad_index != -1 and len(C) < bad_index:
            bad_index = -1

    if depth < 0 and bad_index == -1:
        bad_index = len(C)
    ans.append("Yes" if depth == 0 and bad_index == -1 else "No")
    
for x in ans:
    print(x)