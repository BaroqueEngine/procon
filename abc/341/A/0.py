N = int(input())

ans = []

for i in range(2 * N + 1):
    ans.append(str(1 - i % 2))

print("".join(ans))
