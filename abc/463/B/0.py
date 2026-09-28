N, X = input().split()
N = int(N)

num = ord(X) - ord("A")

for _ in range(N):
    S = input()
    if S[num] == "o":
        print("Yes")
        exit()
print("No")
