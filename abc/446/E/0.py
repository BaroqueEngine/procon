M, A, B = map(int, input().split())

ans = 0
safe = set()
bad = set()

for y in range(M):
    for x in range(M):
        if (x, y) in safe:
            ans += 1
            continue
        if (x, y) in bad:
            continue
        s1 = x
        s2 = y
        if s1 == 0 or s2 == 0:
            continue
        ok = True
        seen = set()
        seen.add((s1, s2))

        while True:
            s3 = (A * s2 + B * s1) % M
            if s3 == 0 or (s2, s3) in bad:
                ok = False
                bad |= seen
                break
            if (s2, s3) in seen or (s2, s3) in safe:
                safe |= seen
                break
            seen.add((s2, s3))
            s1, s2 = s2, s3

        if ok:
            ans += 1

print(ans)