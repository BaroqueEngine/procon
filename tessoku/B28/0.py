N = int(input())
fib = [1, 1]
for _ in range(N - 2):
    fib.append((fib[-1] + fib[-2]) % (10**9+7))
print(fib[-1])
