S = input()

depth = 0
for c in S:
    if c == "(":
        depth += 1
    else:
        depth -= 1
        if depth < 0:
            print("No")
            exit()

if depth == 0:
    print("Yes")
else:
    print("No")
