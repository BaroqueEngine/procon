N = int(input())
A = list(map(int, input().split()))


def prime_factorize(x):
    ret = []
    while x > 0 and x % 2 == 0:
        ret.append(2)
        x //= 2
    v = 3
    while v * v <= x:
        if x % v == 0:
            ret.append(v)
            x //= v
        else:
            v += 2
    if x != 1:
        ret.append(x)
    return sorted(ret)


def babanuki(sorted_arr):
    amari = []
    for x in sorted_arr:
        if len(amari) > 0 and amari[-1] == x:
            amari.pop()
        else:
            amari.append(x)
    ret = 1
    for x in amari:
        ret *= x
    return ret


dic = {}
for x in A:
    v = babanuki(prime_factorize(x))
    if v in dic:
        dic[v] += 1
    else:
        dic[v] = 1

ans = 0

if 0 in dic:
    ans += dic[0] * (N - dic[0])

for x in dic:
    ans += dic[x] * (dic[x] - 1) // 2

print(ans)
