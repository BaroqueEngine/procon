N = int(input())
A = [input().split() for _ in range(N)]
A.sort()

total = 0
for a, b in A:
    total += int(b)

id = total % N
print(A[id][0])
