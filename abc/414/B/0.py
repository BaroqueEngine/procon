N = int(input())
ans = ""
for _ in range(N):
    C, L = input().split()
    L = int(L)
    if len(ans) + L > 100:
        print("Too Long")
        exit()
    ans += C * L

print(ans)