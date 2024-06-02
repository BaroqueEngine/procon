N = int(input())
A, B, C, D = map(int, input().split())
X = int(input().replace(".", ""))

ng = -1
ok = 10**18

# (A + 2B * 3C * 4D) / (A + B + C + D) <= X


def f(num):
    return ((A + B * 2 + C * 3 + D * 4) + num) * 1000 <= X * (A + B + C + D + num)


while (ok - ng) > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)
