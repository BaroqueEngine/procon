N = int(input())
S = input()
A = [x == "#" for x in S]
left = 0
right = 0
for i in range(N):
    if A[i]:
        break
    A[i] = True
    left += 1

for i in range(N - 1, -1, -1):
    if A[i]:
        break
    A[i] = True
    right += 1

def a():
    global A
    NA = A[:]
    for i in range(1, N):
        NA[i - 1] |= A[i]
    A = NA[:]

def b():
    global A
    NA = A[:]
    for i in range(N - 1):
        NA[i + 1] |= A[i]
    A = NA[:]

for _ in range(left):
    a()
for _ in range(right):
    b()

max_cnt = 0
cnt = 0
for i in range(N):
    if not A[i]:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        cnt = 0
left += max(max_cnt, cnt)
print(left, right)
