N, M = map(int, input().split())
A = list(map(int, input().split()))

max_count = 0
max_index = 0
counts = [0] * N

for x in A:
    index = x - 1
    counts[index] += 1
    if counts[index] > max_count:
        max_count = counts[index]
        max_index = index + 1
    elif counts[index] == max_count:
        max_index = min(max_index, index + 1)
    print(max_index)
