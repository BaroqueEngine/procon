import string

N = int(input())
S = input()
Q = int(input())

dic = {}
for c in string.ascii_letters:
    dic[c] = c

for _ in range(Q):
    c, d = input().split()
    for char in string.ascii_letters:
        if dic[char] == c:
            dic[char] = d

ans = []
for c in S:
    ans.append(dic[c])

print("".join(ans))
