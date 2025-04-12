N = int(input())
is_login = False
ans = 0
for _ in range(N):
    S = input()
    if S == "login":
        is_login = True
    elif S == "logout":
        is_login = False
    elif S == "private" and not is_login:
        ans += 1
print(ans)