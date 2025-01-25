p, q = input().split()
A = [3, 1, 4, 1, 5, 9]
S = [0]
for x in A:
    S.append(S[-1] + x)

p = ord(p) - ord("A")
q = ord(q) - ord("A")
print(abs(S[q] - S[p]))