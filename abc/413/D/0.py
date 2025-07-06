from collections import Counter

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == 2:
        ans.append("Yes")
        continue
    l = len(set(A))
    if l == 1:
        ans.append("Yes")
        continue
    if l == 2:
        c = Counter(A)
        keys = list(c.keys())
        values = list(c.values())
        if abs(keys[0]) == abs(keys[1]) and abs(values[0] - values[1]) <= 1:
            ans.append("Yes")
        else:
            ans.append("No")
        continue
    A.sort(key=lambda x: abs(x))
    ok = True
    for i in range(1, N):
        if A[1] * A[i - 1] != A[i] * A[0]:
            ans.append("No")
            ok = False
            break
    if ok:
        ans.append("Yes")


for x in ans:
    print(x)