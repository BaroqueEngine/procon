N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()

result = False
for i in range(N - 1):
    d1, s1, t1 = A[i]
    d2, s2, t2 = A[i + 1]
    if d1 != d2:
        continue
    if t1 > s2:
        result = True

print("Yes" if result else "No")
