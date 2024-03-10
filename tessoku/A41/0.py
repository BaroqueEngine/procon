N = int(input())
S = input()

from itertools import groupby

for key, group in groupby(S):
    if len(list(group)) >= 3:
        print("Yes")
        exit()
print("No")
