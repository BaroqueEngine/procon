N = int(input())
S = "==" if N % 2 == 0 else "="
N -= len(S)
L = R = "-" * (N // 2)
print(L + S + R)