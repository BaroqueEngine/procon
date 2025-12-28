N, M = map(int, input().split())
S = input()
T = input()

def f(a, b):
    ret = 0
    for i in range(len(a)):
        ret += abs(int(a[i]) + 10 - int(b[i])) % 10
    return ret

ans = 10**18
for i in range(N - M + 1):
    ans = min(ans, f(S[i:i+M], T))

print(ans)