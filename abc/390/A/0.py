A = list(map(int, input().split()))

diff = 0
for i in range(5):
    diff += abs((i + 1) - A[i])
print("Yes" if diff == 2 else "No")