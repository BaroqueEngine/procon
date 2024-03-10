N = int(input())

INF = 9999
ans = ""
for i in range(N + 1):
    c = "-"
    num = INF
    for j in range(1, 10):
        if N % j == 0:
            if i % (N // j) == 0:
                num = min(num, j)
    if num == INF:
        ans += c
    else:
        ans += str(num)
print(ans)
