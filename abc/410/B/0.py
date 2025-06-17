N, Q = map(int, input().split())
X = list(map(int, input().split()))
box = [0] * N
balls = []

for x in X:
    if x == 0:
        min_v = min(box)
        for i in range(N):
            if box[i] == min_v:
                box[i] += 1
                balls.append(i + 1)
                break
    else:
        box[x - 1] += 1
        balls.append(x)

print(*balls)