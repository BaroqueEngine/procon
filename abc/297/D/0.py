A, B = map(int, input().split())

ans = 0

while A != B:
    if A == 0 or B == 0:
        ans -= 1
        break
    if A > B:
        cnt = A // B
        ans += cnt
        A -= cnt * B
    else:
        cnt = B // A
        ans += cnt
        B -= cnt * A
print(ans)
