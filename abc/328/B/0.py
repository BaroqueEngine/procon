N = int(input())
D = list(map(int, input().split()))

ans = 0


def check(s):
    return len(set(list(s))) == 1


for month in range(1, N + 1):
    for day in range(1, D[month - 1] + 1):
        if check(str(month) + str(day)):
            ans += 1
print(ans)
