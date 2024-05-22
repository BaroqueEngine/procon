ac = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
}

N = int(input())
for i in range(1, N + 1):
    P, V = input().split()
    if ac[P] == 0 and V == "AC":
        ac[P] = i

for c in "ABCDEF":
    print(ac[c])