S = input()
stack = []
dic = {
    ">": "<",
    ")": "(",
    "]": "["
}

for c in S:
    if c in "([<":
        stack.append(c)
    else:
        if len(stack) == 0 or stack[-1] != dic[c]:
            print("No")
            exit()
        stack.pop()

if len(stack) == 0:
    print("Yes")
else:
    print("No")