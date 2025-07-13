A = int(input())
N = int(input())

def check(x, radix):
    ret = []
    while x > 0:
        ret.append(x % radix)
        x //= radix
    ret.reverse()
    return ret == ret[::-1]

nums = set([])
for i in range(1, 1000000):
    si = str(i)
    x = int(si + si[::-1])
    if x <= N:
        nums.add(x)
    a = si[:-1]
    x = int(a + si[-1] + a[::-1])
    if x <= N:
        nums.add(x)

ans = 0
for x in nums:
    if check(x, A):
        ans += x

print(ans)
