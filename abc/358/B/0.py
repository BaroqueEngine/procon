N, A = map(int, input().split())
T = list(map(int, input().split()))

time = 0
for x in T:
    time = max(time, x) + A
    print(time)
