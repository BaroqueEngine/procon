import collections
N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
print(c[100] * c[400] + c[200] * c[300])
