N, K = map(int, input().split())
S = input()

print("Yes" if K % 2 == S.count("1") % 2 else "No")
