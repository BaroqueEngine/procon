import itertools
S = input()

counts = []
for key, value in itertools.groupby(S):
    counts.append((int(key), len(list(value))))

ans = 0
for i in range(len(counts) - 1):
	if counts[i][0] + 1 == counts[i + 1][0]:
		ans += min(counts[i][1], counts[i + 1][1])
print(ans)