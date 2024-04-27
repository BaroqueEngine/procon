N = int(input())
A = [0] + list(map(int, input().split()))

ans = []
for i in range(1, N + 1):
    B = A[::]
    j = 0
    while True:
        temp = B[i]
        B[i] = i
        i = temp
        j += 1
        if i == B[i]:
            break
    ans.append(j)
print(*ans)
