N = int(input())
S, T = input().split()

ans = ""
for line in zip(*[S, T]):
    for c in line:
        ans += c
print(ans)
