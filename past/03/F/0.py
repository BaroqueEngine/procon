N = int(input())
A = [input() for _ in range(N)]

arr = [None] * N
left = 0
right = N - 1

while left <= right:
    x = A[left]
    y = A[right]
    ok = False
    for c in x:
        if c in y:
            arr[left] = arr[right] = c
            ok = True
            break
    if not ok:
        print(-1)
        exit()
    left += 1
    right -= 1

print("".join(arr))
