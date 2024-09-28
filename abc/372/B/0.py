M = int(input())
A = []

while M > 0:
    i = 0
    while 3 ** (i + 1) <= M:
        i += 1
    A.append(i)
    M -= 3 ** i

print(len(A))
print(*A)
