S = input()
ans = 0

prev = "o"
for cur in S:
    if cur == prev:
        ans += 1
        prev = "i" if prev == "o" else "o"
    prev = "i" if prev == "o" else "o"
if prev == "i":
    ans += 1
print(ans)