N, K = map(int, input().split())
S = input()

num = 0

for c in S:
    if num < K and c == "o":
        num += 1
        print("o", end="")
    else:
        print("x", end="")
print()
