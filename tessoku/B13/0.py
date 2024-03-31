N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
total = 0
ans = 0

while left < N:
    if right < left:
        right = left
        total = 0
    while right < N and total + A[right] <= K:
        total += A[right]
        right += 1

    ans += right - left

    total -= A[left]
    left += 1

print(ans)
