M = int(input())
D = list(map(int, input().split()))
target = sum(D) // 2 + 1

total = 0
for i in range(M):
    if total + D[i] >= target:
        print(i + 1, target - total)
        exit()
    else:
        total += D[i]
