N, M = map(int, input().split())
F = list(map(int, input().split()))

print("Yes" if N == len(set(F)) else "No")
print("Yes" if M == len(set(F)) else "No")