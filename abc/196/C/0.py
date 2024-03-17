N = int(input())

ans = 0
i = 1

while True:
    v = i * (10 ** len(str(i))) + i
    if v <= N:
        ans += 1
    else:
        break
    i += 1

print(ans)
