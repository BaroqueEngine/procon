S = input()
dic = {}
max_cnt = 1

for i in range(len(S) - 1):
    s = S[i:i+2]
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
        max_cnt = max(max_cnt, dic[s])

arr = []
for key in dic:
    if dic[key] == max_cnt:
        arr.append(key)
arr.sort()
print(arr[0])