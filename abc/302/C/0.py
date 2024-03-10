N, M = map(int, input().split())
S = [input() for _ in range(N)]

import itertools

def diff(a, b):
    ret = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ret += 1
    return ret

for v in itertools.permutations(S, N):
    ok = True
    for i in range(N - 1):
        if diff(v[i], v[i + 1]) != 1:
            ok = False
            break
    
    if ok:
        print("Yes")
        exit()
print("No")