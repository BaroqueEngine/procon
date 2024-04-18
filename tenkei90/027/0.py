N = int(input())
seen = set()
for i in range(1, N + 1):
    S = input()
    if S not in seen:
        print(i)
        seen.add(S)
