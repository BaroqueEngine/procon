A, B = map(int, input().split())

ans = 1

if A == B:
    print(1)
    exit()

print(3 if (A + B) % 2 == 0 else 2)
