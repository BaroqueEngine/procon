N = int(input())
bin = []

while N > 0:
    bin.append(N % 2)
    N //= 2

print("".join(map(str, bin[::-1])).zfill(10))
