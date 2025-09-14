N = int(input())
L = list(map(int, input().split()))
left = 0
right = N

for i in range(N):
    if L[i] == 1:
        break
    left += 1

for i in range(N - 1, -1, -1):
    if L[i] == 1:
        break
    right -= 1

print(max(0, right - left - 1))