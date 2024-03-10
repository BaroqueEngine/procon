A = input()
B = input()

from collections import defaultdict
dic_a = defaultdict(int)
dic_b = defaultdict(int)

for c in A:
    dic_a[c] += 1

for c in B:
    dic_b[c] += 1

atcoder = list("atcoder")

for i in range(ord("a"), ord("z") + 1):
    char = chr(i)
    while dic_a[char] >= 1:
        dic_a[char] -= 1
        if dic_b[char] >= 1:
            dic_b[char] -= 1
        else:
            if char in atcoder and dic_b["@"] >= 1:
                dic_b["@"] -= 1
            else:
                print("No")
                exit()

    while dic_b[char] >= 1:
        dic_b[char] -= 1
        if dic_a[char] >= 1:
            dic_a[char] -= 1
        else:
            if char in atcoder and dic_a["@"] >= 1:
                dic_a["@"] -= 1
            else:
                print("No")
                exit()
print("Yes")  