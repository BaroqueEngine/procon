S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = int(input())
if N == 0:
    print(0)
    exit()

ans = ""
while N > 0:
    ans += S[N % 36]
    N //= 36
print(ans[::-1])
