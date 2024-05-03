T = ["axa", "ixi", "uxu", "exe", "oxo"]
N = int(input())
S = input()

for t in T:
    S = S.replace(t, "...")
print(S)
