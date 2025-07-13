A = int(input())
N = int(input())

nums = set([])
for i in range(1, 1000000):
    s1 = int(str(i) + str(i)[::-1])
    s2 = int(str(i) + str(i)[:-1][::-1])

    if s1 <= N:
        nums.add(s1)
    
    if s2 <= N:
        nums.add(s2)

def is_palindrome(x):
    ret = []
    while x > 0:
        ret.append(x % A)
        x //= A
    return ret == ret[::-1]

ans = 0
for x in nums:
    if is_palindrome(x):
        ans += x

print(ans)