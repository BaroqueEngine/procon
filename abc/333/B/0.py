S = input()
T = input()


def dist(a):
    start = ord(a[0]) - ord('A')
    end = ord(a[1]) - ord('A')
    if start > end:
        start, end = end, start
    diff = end - start
    if diff >= 3:
        diff = 5 - diff
    return diff


print("Yes" if dist(S) == dist(T) else "No")
