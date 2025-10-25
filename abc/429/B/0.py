N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
diff = total - M
print("Yes" if diff in A else "No")