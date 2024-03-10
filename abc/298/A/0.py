N = int(input())
S = input()

ok = False
for c in S:
    if c == "x":
        print("No")
        exit()
    elif c == "o":
        ok = True

print("Yes" if ok else "No")
