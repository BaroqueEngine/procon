N = int(input())
tak, aoki = 0, 0

for _ in range(N):
    X, Y = map(int, input().split())
    tak += X
    aoki += Y

if tak == aoki:
    print("Draw")
elif tak > aoki:
    print("Takahashi")
else:
    print("Aoki")
