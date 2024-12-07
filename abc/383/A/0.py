N = int(input())

time = 0
water = 0
for _ in range(N):
    T, V = map(int, input().split())
    water = max(0, water - (T - time))
    water += V
    time = T
print(water)
