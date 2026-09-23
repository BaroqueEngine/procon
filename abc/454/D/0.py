def convert(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 4 and stack[-4:] == list("(xx)"):
            for _ in range(4):
                stack.pop()
            for _ in range(2):
                stack.append("x")
    return "".join(stack)

ans = []
T = int(input())
for _ in range(T):
    A = convert(input())
    B = convert(input())
    ans.append("Yes" if A == B else "No")

for x in ans:
    print(x)