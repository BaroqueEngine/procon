N, K = map(int, input().split())
dic = {}
for _ in range(N):
    S = input()
    if S in dic:
        dic[S] += 1
    else:
        dic[S] = 1

cnt = []
for key in dic:
    cnt.append(dic[key])
cnt.sort(reverse=True)
num = cnt[K - 1]

ans = []
for key in dic:
    if dic[key] == num:
        ans.append(key)

if len(ans) == 1:
    print(ans[0])
else:
    print("AMBIGUOUS")