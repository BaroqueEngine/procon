A = list(map(int, input().split()))

while len(A) < 10:
    x = A[-2] + A[-1]
    sx = str(x)
    rx = sx[::-1]
    nx  = int(rx)
    A.append(nx)

print(A[-1])