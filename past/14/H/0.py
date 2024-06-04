N = int(input())
A = list(map(int, input().split()))

dic = {}
for x in A:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

S = sorted(list(set(A)))
for i in range(len(S) - 3 + 1):
    if (S[i] + 1 == S[i + 1] == S[i + 2] - 1) and (S[i] in dic and S[i + 1] in dic and S[i + 2] in dic):
        min_v = min(dic[S[i]], dic[S[i + 1]], dic[S[i + 2]])
        dic[S[i]] -= min_v
        dic[S[i + 1]] -= min_v
        dic[S[i + 2]] -= min_v

ans = 0
for k, v in dic.items():
    ans += v
print(ans)
