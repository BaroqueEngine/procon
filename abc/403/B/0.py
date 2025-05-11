T = input()
U = input()

for i in range(len(T) - len(U) + 1):
    found = True
    for j in range(len(U)):
        if not(T[i + j] == "?" or T[i + j] == U[j]):
            found = False
            break
    if found:
        print("Yes")
        exit()
print("No")
