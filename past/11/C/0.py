N, M = map(int, input().split())
ans = ""

for i in range(1, M + 1):
    if i >= 2 and ans[-1] == "x":
        ans += "x"
    else:
        ans += "o" if (N ** i) <= (10**9) else "x"
print(ans)