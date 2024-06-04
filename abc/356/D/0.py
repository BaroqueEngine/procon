N, M = map(int, input().split())
mod = 998244353

"""
0000
0001
0010
0011
0100
0101
0110
0111
1000
"""

ans = 0
for bit in range(60):
    if M >> bit & 1 == 0:
        continue
    # bit毎の連続する1の数, 01の数
    num1 = 2**bit
    num01 = num1 * 2
    ans += N // num01 * num1
    remain = N % num01
    remain = max(0, remain - num1 + 1)
    ans += remain
    ans %= mod

print(ans)
