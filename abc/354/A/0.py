H = int(input())
height = 0
for i in range(100):
    height += 2 ** i
    if height > H:
        print(i + 1)
        exit()
