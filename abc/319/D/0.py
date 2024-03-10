N, M = map(int, input().split())
L = list(map(int, input().split()))
max_word_length = 0
for l in L:
    max_word_length = max(max_word_length, l)

ng = 0
ok = 10**18


def f(max_width):
    if max_word_length > max_width:
        return False

    line = 1
    width = 0

    for i in range(N):
        if width + L[i] <= max_width:
            width += L[i]
        else:
            line += 1
            width = L[i]

        # スペース処理
        if i < N - 1:
            if width == max_width:
                line += 1
                width = 0
            else:
                width += 1

    return line <= M


while abs(ng - ok) > 1:
    mid = (ng + ok) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
