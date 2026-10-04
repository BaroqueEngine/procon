N = int(input())
X = list(map(int, input().split()))

print("Yes" if max(X) <= -1 else "No")