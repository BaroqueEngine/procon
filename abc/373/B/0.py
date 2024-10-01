S = input()
pos = S.index("A")
ans = 0

for i in range(1, 26):
    char = chr(ord("A") + i)
    new_pos = S.index(char)
    ans += abs(new_pos - pos)
    pos = new_pos
print(ans)
