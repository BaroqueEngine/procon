S = input()
T = input()

for i in range(1, len(S)):
    c = S[i]
    if c.isupper() and S[i - 1] not in T:
        print("No")
        exit()

print("Yes")
