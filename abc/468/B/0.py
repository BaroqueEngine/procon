M, D = map(int, input().split())
S = list(input())

for i in range(M):
    if S[i] == "G":
        for j in range(max(0, i - D), i):
            if S[j] == ".":
                S[j] = "x"
        for j in range(i + 1, min(M, i + D + 1)):
            if S[j] == ".":
                S[j] = "x"

st = "".join(S)
print(st.count("."))
