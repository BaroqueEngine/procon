A = list(map(int, input().split()))
dic = {}
for x in A:
    dic[x] = dic.get(x, 0) + 1

T = []
for k, v in dic.items():
    T.append((k, v))
T.sort(key=lambda x: -x[1])

if len(T) >= 2 and T[0][1] >= 3 and T[1][1] >= 2:
    print("Yes")
else:
    print("No")