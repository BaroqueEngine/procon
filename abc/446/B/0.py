N, M = map(int, input().split())
juices = [True] * (M + 1)
ans = []

for _ in range(N):
    L = int(input())
    X = list(map(int, input().split()))

    for x in X:
        if juices[x]:
            ans.append(x)
            juices[x] = False
            found = True
            break
    else:
        ans.append(0)

for x in ans:
    print(x)