ans = 0

for i in range(1, 13):
    S = input()
    if len(S) == i:
        ans += 1

print(ans)
