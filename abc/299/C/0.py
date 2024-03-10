import itertools

N = int(input())
S = input()
ans = 0


def search(S):
    global ans
    G = itertools.groupby(S)

    prev_bar = False
    for key, group in G:
        if key == "-":
            prev_bar = True
        else:
            if prev_bar:
                ans = max(ans, len(list(group)))
            prev_bar = False


search(list(S))
search(reversed(list(S)))

if ans == 0:
    ans = -1

print(ans)
