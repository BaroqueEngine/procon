S = input()
S = list(S[::-1])

for i in range(len(S) - 2 + 1):
    if S[i] == "A" and S[i + 1] == "W":
        S[i] = "C"
        S[i + 1] = "A"

S = S[::-1]
print("".join(S))