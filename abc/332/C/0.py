N, M = map(int, input().split())
S = list(map(int, list(input())))

ans = 0
muji = M
logo = 0

i = 1

for x in S:
    if x == 0:
        muji = M
        logo = ans
    elif x == 1:
        if muji > 0:
            muji -= 1
        elif logo > 0:
            logo -= 1
        else:
            ans += 1
    else:
        if logo > 0:
            logo -= 1
        else:
            ans += 1

    # print("{}日目 {} {} {}".format(i, muji, logo, ans))
    i += 1

print(ans)
