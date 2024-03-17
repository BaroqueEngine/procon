N, X = map(int, input().split())
A = list(map(int, input().split()))

print("Yes" if any([x == X for x in A]) else "No")
