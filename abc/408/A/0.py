N, S = map(int, input().split())
T = [0] + list(map(int, input().split()))

for i in range(len(T) - 1):
    if T[i + 1] - T[i] > S:
        print("No")
        exit()

print("Yes") 