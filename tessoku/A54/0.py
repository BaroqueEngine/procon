dic = dict()

Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        dic[query[1]] = query[2]
    else:
        print(dic[query[1]])
