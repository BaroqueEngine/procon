N = int(input())

ans = ""
for i in range(1, N + 1):
    ans += "x" if i % 3 == 0 else "o"
print(ans)
