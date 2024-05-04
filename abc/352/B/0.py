S = input()
T = input()

ans = []
pos = 0

for i in range(len(T)):
    if S[pos] == T[i]:
        ans.append(i + 1)
        pos += 1
print(*ans)
