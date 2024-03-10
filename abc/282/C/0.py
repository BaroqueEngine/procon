N = int(input())
S = list(input())

kakko = False
for i in range(N):
    if S[i] == '"':
        kakko = not kakko
    elif S[i] == "," and not kakko:
        S[i] = "."

print("".join(S))
