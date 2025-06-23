N = int(input())
D = list(map(int, input().split()))

for i in range(N - 1):
    line = [D[i]]
    for j in range(i + 1, N - 1):
        line.append(line[-1] + D[j])
    print(*line)