N = int(input())
is_prime = [True] * (N + 1)
for i in range(2, N + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, N + 1, i):
        is_prime[j] = False

for i in range(2, N + 1):
    if is_prime[i]:
        print(i)
