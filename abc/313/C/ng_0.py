N = int(input())
A = list(map(int, input().split()))
avg = sum(A) / N
avg_int = sum(A) // N

if avg == avg_int:
    total = 0
    for x in A:
        total += abs(avg_int - x)
    print(total // 2)
elif avg > avg_int:
    first = True
    total = 0
    for x in A:
        if x > avg_int and first:
            first = False
            total += abs(avg_int - x + 1)
        else:
            total += abs(avg_int - x)
    print(total // 2)
else:
    first = True
    total = 0
    for x in A:
        if x < avg_int and first:
            first = False
            total += abs(avg_int - x - 1)
        else:
            total += abs(avg_int - x)
    print(total // 2)
