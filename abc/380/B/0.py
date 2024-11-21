S = input()
A = S.split("|")
A.pop(0)
A.pop()

ans = []
for x in A:
    ans.append(len(x))
print(*ans)
