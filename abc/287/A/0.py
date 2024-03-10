N = int(input())
cnt = sum([input() == "For" for _ in range(N)])

print("Yes" if cnt >= N // 2 + 1 else "No")
