N, X = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict

dic = defaultdict(int)
for x in A:
    dic[x] += 1

if X == 0:
    for key in dic:
        if dic[key] >= 2:
            print("Yes")
            exit()

for x in A:
    if dic[x + X] >= 1:
        print("Yes")
        exit()
print("No")
