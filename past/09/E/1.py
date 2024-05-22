S = input()

time = 500
prev = int(S[0])

left = [1, 2, 3, 4, 5]
right = [6, 7, 8, 9, 0]

for i in range(1, len(S)):
    cur = int(S[i])
    if cur == prev:
        time += 301
    elif (cur in left) == (prev in left):
        time += 210
    else:
        time += 100
    prev = cur
print(time)
    