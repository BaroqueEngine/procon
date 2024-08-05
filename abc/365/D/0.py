N = int(input())
S = input()

cur = [0, 0, 0]  # グー・チョキ・パー

for hand in S:
    next = cur[:]
    if hand == "P":
        next[1] = max(cur[0], cur[2]) + 1
        next[2] = max(cur[0], cur[1])
    elif hand == "R":
        next[2] = max(cur[0], cur[1]) + 1
        next[0] = max(cur[1], cur[2])
    else:
        next[0] = max(cur[1], cur[2]) + 1
        next[1] = max(cur[0], cur[2])

    cur = next[:]

print(max(cur))
