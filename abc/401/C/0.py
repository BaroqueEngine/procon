N, K = map(int, input().split())
MOD = 10**9
arr = [1] * K
arr.append(K)
while len(arr) <= N:
    x = arr[-1] * 2 - arr[-(K + 1)]
    x %= MOD
    arr.append(x)

print(arr[N])