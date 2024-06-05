H, W = map(int, input().split())
bmi = W
K = (H / 100)**2

if bmi < 20 * K:
    print("A")
elif 20 * K <= bmi < 25 * K:
    print("B")
else:
    print("C")
