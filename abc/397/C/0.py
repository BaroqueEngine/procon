N = int(input())
A = list(map(int, input().split()))
dic_a = {}
dic_b = {}
num_a = 0
num_b = 0

for x in A:
    dic_b[x] = dic_b.get(x, 0) + 1
    if dic_b[x] == 1:
        num_b += 1

ans = 0
for x in A:
    dic_a[x] = dic_a.get(x, 0) + 1
    if dic_a[x] == 1:
        num_a += 1
    dic_b[x] -= 1
    if dic_b[x] == 0:
        num_b -= 1
    ans = max(ans, num_a + num_b)

print(ans)