N = int(input())

u = -1
max_dist = 0
for i in range(2, N + 1):
    print("? {0} {1}".format(1, i), flush=True)
    dist = int(input())
    if max_dist < dist:
        max_dist = dist
        u = i

max_dist = 0
for i in range(1, N + 1):
    if i == u:
        continue
    print("? {0} {1}".format(u, i), flush=True)
    dist = int(input())
    if max_dist < dist:
        max_dist = dist
print("! {}".format(max_dist))
