N = int(input())
A = [input().split() for _ in range(N)]

min_i = 0
min_age = 1000000000000
for i in range(N):
    A[i][1] = int(A[i][1])
    if A[i][1] < min_age:
      min_i = i
      min_age = A[i][1]

for i in range(N):
   index = (min_i + i) % N
   print(A[index][0])