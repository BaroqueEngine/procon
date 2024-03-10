import string
import collections
S = input()
dic = collections.defaultdict(int)

max_count = 0
for c in S:
    dic[c] += 1
    max_count = max(max_count, dic[c])

for c in string.ascii_lowercase:
    if dic[c] == max_count:
        print(c)
        exit()
