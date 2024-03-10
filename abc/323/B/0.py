N = int(input())
result = []
for i in range(N):
    result.append((input().count("o"), i))
result.sort(key=lambda x: (-x[0], x[1]))

print(*[index + 1 for _, index in result])
