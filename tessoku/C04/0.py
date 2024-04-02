N = int(input())

divisor = []
for i in range(1, N + 1):
    if i * i > N:
        break
    if N % i == 0:
        divisor.append(i)
        if i * i != N:
            divisor.append(N // i)

for x in sorted(divisor):
    print(x)