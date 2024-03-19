N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
ans = 0

while left < N - 1:
    while right < N - 1 and abs(A[left] - A[right + 1]) <= K:
        right += 1
    ans += right - left
    left += 1

print(ans)
