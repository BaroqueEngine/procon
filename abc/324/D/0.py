N = int(input())
S = input()


def f(s: str):
    return "".join(sorted(list(s))).zfill(len(S))


S = f(S)

ans = 0
for i in range(0, 10**7):
    num = str(i * i)
    if len(num) > 13:
        break
    if S == f(str(num)):
        ans += 1

print(ans)
