N = int(input())
ans = 1

for i in range(1, 10 ** 6 + 1):
    k = i * i * i
    str_k = str(k)
    if k <= N and str_k == str_k[::-1]:
        ans = k

print(ans)
