N = int(input())
words = [input() for _ in range(N)]
ok = True
for i in range(1, N):
    if not ok:
        print("No")
        exit()
    if words[i - 1] == words[i] and words[i] == "sweet":
        ok = False
print("Yes")
