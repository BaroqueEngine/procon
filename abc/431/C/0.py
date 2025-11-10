N, M, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

cnt = 0
while len(B) > 0:
    found = False
    while len(A) > 0:
        if B[-1] >= A[-1]:
            B.pop()
            A.pop()
            cnt += 1
            found = True
            break
        A.pop()
    if not found:
        B.pop()

print("Yes" if cnt >= K else "No")