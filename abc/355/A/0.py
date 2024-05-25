A, B = map(int, input().split())
arr = [1, 2, 3]
arr.remove(A)

if B not in arr:
    print(-1)
    exit()
arr.remove(B)

print(arr[0])
