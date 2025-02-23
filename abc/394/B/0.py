N = int(input())
A = [input() for _ in range(N)]
A.sort(key=lambda x: len(x))

ans = ""
for x in A:
    ans += x
print(ans)