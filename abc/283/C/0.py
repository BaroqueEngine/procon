S = list(input())
length = len(S)

A = []
cnt = 0
while len(S) > 0:
    A.append(S.pop())
    if len(A) >= 2 and A[-1] == "0" and A[-2] == "0":
        cnt += 1
        A.pop()
        A.pop()

print(length - cnt)
