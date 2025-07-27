S = input()
T = []
ready = True

for i in range(len(S)):
    if S[i] == "#":
        T.append("#")
        ready = True
    else:
        if ready:
            ready = False
            T.append("o")
        else:
            T.append(".")  

print("".join(T))