X = int(input())
total = 1
for i in range(2, 100):
    total *= i
    if total == X:
        print(i)
        exit()