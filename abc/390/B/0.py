from fractions import Fraction
N = int(input())
A = list(map(int, input().split()))

S = []
for i in range(N - 1):
    S.append(Fraction(A[i + 1], A[i]))

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        print("No")
        exit()
print("Yes")