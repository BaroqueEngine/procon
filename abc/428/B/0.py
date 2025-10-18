N, K = map(int, input().split())
S = input()

dic = {}
max_cnt = 0

for i in range(N - K + 1):
    word = S[i:i+K]
    dic[word] = dic.get(word, 0) + 1
    max_cnt = max(dic[word], max_cnt)

ans = []
for key in dic:
    if dic[key] == max_cnt:
        ans.append(key)
ans.sort()

print(max_cnt)
print(*ans)