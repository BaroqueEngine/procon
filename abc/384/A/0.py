N, C1, C2 = input().split()
S = list(input())

for i in range(int(N)):
    if S[i] != C1:
        S[i] = C2
print("".join(S))
