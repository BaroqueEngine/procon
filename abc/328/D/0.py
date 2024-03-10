S = list(input())

ans = []

for x in S:
    ans.append(x)
    while len(ans) >= 3 and "".join(ans[-3:]) == "ABC":
        ans.pop()
        ans.pop()
        ans.pop()
print("".join(ans))
