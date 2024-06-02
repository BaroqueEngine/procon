A, B, C, D = map(int, input().split())
X = A * D
Y = B * C
cnt = 0
if D < 0:
    cnt += 1
if B < 0:
    cnt += 1

if X == Y:
    print("=")
elif X > Y:
    print("><"[cnt % 2])
else:
    print("<>"[cnt % 2])
