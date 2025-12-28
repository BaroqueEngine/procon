N = int(input())
A = list(map(int, input().split()))
stack = []

for x in A:
    stack.append(x)
    while len(stack) >= 4 and (stack[-1] == stack[-2] == stack[-3] == stack[-4]):
        for _ in range(4):
            stack.pop()

print(len(stack))
