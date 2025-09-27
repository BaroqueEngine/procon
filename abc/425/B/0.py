import itertools
N = int(input())
A = list(map(int, input().split()))

arr = [i for i in range(1, N + 1)]
for p in itertools.permutations(arr):
    ok = True
    for i in range(N):
        if A[i] == -1:
            continue
        if A[i] != p[i]:
            ok = False
    
    if ok:
        print("Yes")
        print(*p)
        exit()

print("No")