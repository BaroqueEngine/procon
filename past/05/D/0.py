N = int(input())
arr = [input() for _ in range(N)]
max_len = max([len(s) for s in arr])
arr = [[x.zfill(max_len), x] for x in arr]
arr.sort(key=lambda x: (x[0], -len(x[1])))
for x in arr:
    print(x[1])