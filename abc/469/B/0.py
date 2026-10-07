N = int(input()) + 2
S = "x" + input() + "x"

ans = 0
for i in range(1, N - 1):
    index = i - 1
    if S[index : index + 3] == "xxx":
        ans += 1

print(ans)