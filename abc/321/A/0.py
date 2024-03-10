S = list(map(int, list(input())))
ok = True

for i in range(len(S) - 1):
    if S[i] <= S[i + 1]:
        ok = False

print("Yes" if ok else "No")
