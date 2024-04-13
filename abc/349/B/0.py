import string
S = input()
dic = {}
for c in string.ascii_lowercase:
    dic[c] = 0

for c in S:
    dic[c] += 1

for i in range(1, 101):
    cnt = 0
    for c in string.ascii_lowercase:
        if dic[c] == i:
            cnt += 1
    if not cnt == 0 and not cnt == 2:
        print("No")
        exit()
print("Yes")
