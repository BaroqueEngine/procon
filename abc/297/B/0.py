S = input()

pos = []
for i in range(len(S)):
    if S[i] == "B":
        pos.append(i)

if pos[0] % 2 == pos[1] % 2:
    print("No")
    exit()

r_count = 0
for s in S:
    if s == "R":
        r_count += 1
    elif s == "K":
        break

print("Yes" if r_count == 1 else "No")
