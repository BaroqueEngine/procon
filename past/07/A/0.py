S = input()
v = 0
for i in range(0, len(S) - 1, 2):
    v += int(S[i])
v *= 3

for i in range(1, len(S) - 1, 2):
    v += int(S[i])
v %= 10
print("Yes" if v == int(S[-1]) else "No")
