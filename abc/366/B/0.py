N = int(input())
S = [input() for _ in range(N)]

max_len = len(S[0])
for i in range(1, N):
    asta_num = max(0, max_len - len(S[i]))
    S[i] += "*" * asta_num
    max_len = max(max_len, len(S[i]))

S = S[::-1]
for i in range(max_len):
    line = ""
    for j in range(N):
        if i < len(S[j]):
            line += S[j][i]
    print(line)
