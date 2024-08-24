N = int(input())
H = list(map(int, input().split()))
T = 0

for x in H:
    combo = x // 5
    x -= combo * 5
    T += combo * 3
    while x > 0:
        if T % 3 == 2:
            x -= 3
        else:
            x -= 1
        T += 1
print(T)
