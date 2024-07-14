A = list(map(int, input().split()))
C = input()

if C == "Red":
    A.pop(0)
elif C == "Green":
    A.pop(1)
else:
    A.pop(2)

print(min(A))
