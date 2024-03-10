N, M = map(int, input().split())
A = list(map(int, input().split()))

stack = []
ans = []
num = 1

while num <= N:
    stack.append(num)
    if num not in A:
        while len(stack) > 0:
            ans.append(stack.pop())
    num += 1

while len(stack) > 0:
    ans.append(stack.pop())
print(*ans)
