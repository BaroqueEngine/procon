N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

dic = {}
for a, c in A:
    if c not in dic:
        dic[c] = a
    else:
        dic[c] = min(dic[c], a)

ans = 0
for key in dic:
    ans = max(ans, dic[key])
print(ans)
