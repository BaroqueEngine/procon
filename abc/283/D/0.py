S = input()
A = [[]]
seen = set()

for c in S:
    if c == "(":
        A.append([])
    elif c == ")":
        for x in A[-1]:
            seen.remove(x)
        A.pop()
    else:
        if c in seen:
            print("No")
            exit()
        A[-1].append(c)
        seen.add(c)

print("Yes")
