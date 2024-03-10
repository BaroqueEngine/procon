S = input()
A = []
for c in S:
    A.append(ord(c) - ord('A'))

cur = 0
for x in A:
    if cur > x:
        print("No")
        exit()
    cur = x
print("Yes")
