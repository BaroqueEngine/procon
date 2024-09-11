S = input()
T = input()

ans = []

while S != T:
    cand = []
    for i in range(len(S)):
        if S[i] != T[i]:
            word = list(S)
            word[i] = T[i]
            word = "".join(word)
            cand.append(word)
    cand.sort()
    ans.append(cand[0])
    S = cand[0]

print(len(ans))
for word in ans:
    print(word)
