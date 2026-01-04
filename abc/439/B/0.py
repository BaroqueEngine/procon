N = int(input())

def get_happy_number(x):
    arr = []
    while x > 0:
        arr.append(x % 10)
        x //= 10
    ret = 0
    for num in arr:
        ret += num * num
    return ret

for _ in range(100000):
    N = get_happy_number(N)
    if N == 1:
        print("Yes")
        exit()

print("No")