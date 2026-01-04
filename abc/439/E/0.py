import bisect
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort(key=lambda x: (x[0], -x[1]))

lis = [A[0][1]]
for _, b in A[1:]:
    if lis[-1] < b:
        lis.append(b)
    else:
        pos = bisect.bisect_left(lis, b)
        lis[pos] = b

print(len(lis))