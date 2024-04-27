N = int(input())
A = list(map(int, input().split()))

D = []

for x in A:
    D.append(x)
    while len(D) >= 2:
        if D[-2] == D[-1]:
            D.pop()
            D[-1] += 1
        else:
            break

print(len(D))
