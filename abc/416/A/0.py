N, L, R = map(int, input().split())
S = input()

ok = True
for i in range(L - 1, R):
    if S[i] == "x":
        ok = False
        break

print("Yes" if ok else "No")