S = input()
ok = True
for i in range(1, 16, 2):
    if S[i] == "1":
        ok = False
print("Yes" if ok else "No")
