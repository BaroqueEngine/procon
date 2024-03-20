A, B = input().split()
A = int(A)
v = A * int(B.replace(".", ""))

pos = B.find(".")
if pos != -1:
    k = len(B) - 1 - pos
    v //= 10 ** k
print(v)
