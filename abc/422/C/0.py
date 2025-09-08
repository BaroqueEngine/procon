T = int(input())
ans = []
for _ in range(T):
    A, B, C = map(int, input().split())
    ok = 0
    ng = max(A, B, C) + 1
    while (ng - ok) > 1:
        mid = ok + (ng - ok) // 2
        remain_a = A - mid
        remain_c = C - mid
        if remain_a >= 0 and remain_c >= 0 and (remain_a + remain_c + B) >= mid:
            ok = mid
        else:
            ng = mid
    ans.append(ok)

for x in ans:
    print(x)