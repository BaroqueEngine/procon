N = int(input())
ans = []
for i in range(1, N + 1):
    if i * i > N:
        break
    if N % i == 0:
        ans.append(i)
        if i * i != N:
            ans.append(N // i)
for x in sorted(ans):
    print(x)
