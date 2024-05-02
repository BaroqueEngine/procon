from collections import deque
N = int(input())
S = input()
A = deque()

def error():
    print("ERROR")

for i in range(1, N + 1):
    s = S[i - 1]
    if s == "L":
        A.appendleft(i)
    elif s == "R":
        A.append(i)
    elif s == "A":
        if len(A) == 0:
            error()
        else:
            print(A.popleft())
    elif s == "B":
        if len(A) <= 1:
            error()
        else:
            print(A[1])
            first = A.popleft()
            A.popleft()
            A.appendleft(first)
    elif s == "C":
        if len(A) <= 2:
            error()
        else:
            print(A[2])
            first = A.popleft()
            second = A.popleft()
            A.popleft()
            A.appendleft(second)
            A.appendleft(first)
    elif s == "D":
        if len(A) == 0:
            error()
        else:
            print(A.pop())
    elif s == "E":
        if len(A) <= 1:
            error()
        else:
            print(A[-2])
            first = A.pop()
            A.pop()
            A.append(first)
    elif s == "F":
        if len(A) <= 2:
            error()
        else:
            print(A[-3])
            first = A.pop()
            second = A.pop()
            A.pop()
            A.append(second)
            A.append(first)
