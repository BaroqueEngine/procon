N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
cnt_a = 0
cnt_b = 0

ans = 0
while len(A) > 0 and A[-1] > 0:
    ans += A.pop()
    cnt_a += 1

while len(B) > 0 and B[-1] > 0 and cnt_b < cnt_a:
    ans += B.pop()
    cnt_b += 1

while len(A) > 0 and len(B) > 0 and A[-1] + B[-1] > 0:
    ans += A.pop()
    ans += B.pop()

print(ans)