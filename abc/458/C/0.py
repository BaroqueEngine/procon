S = input()

ans = 0
for i in range(len(S)):
    if S[i] == "C":
        left = i + 1
        right = len(S) - i
        ans += min(left, right)

print(ans)