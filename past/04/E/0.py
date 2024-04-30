from itertools import permutations

N = int(input())
S = input()

for c in permutations(S):
    x = "".join(c)
    if x == S:
        continue
    if x[::-1] == S:
        continue
    print(x)
    exit()
print("None")