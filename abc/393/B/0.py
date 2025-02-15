S = input()
ans = 0
for t in range(1, len(S)):
    for i in range(len(S)):
        j = i + t
        k = i + t * 2
        if j < len(S) and k < len(S) and S[i] == "A" and S[j] == "B" and S[k] == "C":
            ans += 1
print(ans)
