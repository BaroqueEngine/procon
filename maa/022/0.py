import collections
N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

ans = 0
for key in c:
    if key == 50000:
        ans += c[key] * (c[key] - 1) // 2
    elif key < 100000 - key:
        ans += c[key] * c[100000 - key]

print(ans)
