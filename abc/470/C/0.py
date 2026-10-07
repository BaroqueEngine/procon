N, Q = map(int, input().split())

A = [0] * N
ids = set()
ans = []
cur = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i = query[1] - 1
        cur ^= A[i]
        A[i] += 1
        if A[i] == 1:
            ids.add(i)
        cur ^= A[i]
        ans.append(cur)        
    else:
        remove_ids = []
        for i in ids:
            cur ^= A[i]
            A[i] -= 1
            if A[i] == 0:
                remove_ids.append(i)
            else:
                cur ^= A[i]
        for i in remove_ids:
            ids.remove(i)
        ans.append(cur)

for x in ans:
    print(x)
