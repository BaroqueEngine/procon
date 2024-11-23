N = int(input())
S = input()
ans = 0

for i in range(N):
    if S[i] != "/":
        continue
    count = 1
    for j in range(1, 10**10):
        if i - j < 0 or i + j >= N:
            break
        if S[i - j] != "1" or S[i + j] != "2":
            break
        count += 2
    ans = max(ans, count)

print(ans)
