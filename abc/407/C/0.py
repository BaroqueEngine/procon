S = list(map(int, list(input())))
cnt = 0
ans = 0

while len(S) > 0:
    x = S.pop()
    x -= cnt
    x %= 10
    ans += 1
    cnt += x
    ans += x

print(ans)