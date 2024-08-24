A, B, C = map(int, input().split())

if C < B:
    C += 24

for i in range(B, C + 1):
    i %= 24
    if i == A:
        print("No")
        exit()
print("Yes")
