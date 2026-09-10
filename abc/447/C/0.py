import re

S = input()
T = input()

if S.replace("A", "") != T.replace("A", ""):
    print(-1)
    exit()

S = re.sub(r"[^A]", "|", S).split("|")
T = re.sub(r"[^A]", "|", T).split("|")

ans = 0
for i in range(len(S)):
    ans += abs(len(S[i]) - len(T[i]))

print(ans)