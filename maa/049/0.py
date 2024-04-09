N = int(input())
fib = [1, 1]

for _ in range(N - 2):
    fib.append((fib[-2] + fib[-1]) % (10**9+7))
print(fib[-1])
