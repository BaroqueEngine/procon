is_prime = [True] * (300000 + 1)
N = len(is_prime)

for i in range(2, N):
    if not is_prime[i]:
        continue
    for j in range(i * 2, N, i):
        is_prime[j] = False

Q = int(input())
for _ in range(Q):
    X = int(input())
    print("Yes" if is_prime[X] else "No")