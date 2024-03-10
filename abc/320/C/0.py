import itertools
M = int(input())
S = [input() for _ in range(3)]


INF = 10 ** 15
ans = INF
for i in range(10):
    ok = True
    for s in S:
        if s.find(str(i)) == -1:
            ok = False
            break
    if not ok:
        continue

    for p in itertools.permutations([0, 1, 2]):
        time = 0
        for index in p:
            reel = S[index]
            while reel[time % M] != str(i):
                time += 1
            time += 1
        time -= 1
        ans = min(ans, time)


print(ans if ans != INF else -1)
