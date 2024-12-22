N, S = map(int, input().split())
A = list(map(int, input().split()))
repeat = S // sum(A)
S -= repeat * sum(A)

if S == 0:
    print("Yes")
    exit()

A = A + A
N = len(A)

right = 0
total = 0

for left in range(N):
    while right < N and total + A[right] <= S:
        total += A[right]
        right += 1
        if total == S:
            print("Yes")
            exit()

    if left == right:
        right += 1
    else:
        total -= A[left]
print("No")
