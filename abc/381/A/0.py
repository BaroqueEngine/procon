N = int(input())
S = input()

if N % 2 == 0:
    print("No")
    exit()

if S.count("/") != 1:
    print("No")
    exit()

L, R = S.split("/")

if L.count("1") != N // 2:
    print("No")
    exit()
if R.count("2") != N // 2:
    print("No")
    exit()

print("Yes")
