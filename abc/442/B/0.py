Q = int(input())
volume = 0
is_playing = False
ans = []
for _ in range(Q):
    A = int(input())
    if A == 1:
        volume += 1
    elif A == 2:
        volume = max(volume - 1, 0)
    else:
        is_playing = not is_playing
    
    ans.append("Yes" if volume >= 3 and is_playing else "No")

for x in ans:
    print(x)