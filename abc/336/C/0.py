N = int(input()) - 1
if N == 0:
    print(0)
    exit()
digits = []
while N > 0:
    digits.append(N % 5)
    N //= 5
digits.reverse()
digits = int("".join(list(map(str, digits)))) * 2
print(digits)
