N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 0

while len(A) > 0 and len(B) > 0:
    found = False
    while len(B) > 0:
        if B[-1] <= A[-1] * 2:
            found = True
            ans += 1
            A.pop()
            B.pop()
            break
        B.pop()
    if not found:
        break

print(ans)
