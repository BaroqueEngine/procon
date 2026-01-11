import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

C = []
for i in range(N):
    C.append(A[i] - (i + 1))

ans = []
for _ in range(Q):
    X, Y = map(int, input().split())
    
    # X未満に欠番が何個あるか
    index_X = bisect.bisect_left(A, X)
    count_before_X = (X - 1) - index_X
    
    # 探すべき欠番のインデックス
    target = count_before_X + Y
    
    index = bisect.bisect_left(C, target)
    ans.append(target + index)

for x in ans:
    print(x)