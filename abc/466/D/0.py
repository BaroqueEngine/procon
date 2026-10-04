N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(M)]
A.reverse()

use_x = set()
use_y = set()
ans = 0

for y, x in A:
    if y not in use_y and x not in use_x:
        ans += 1
    use_y.add(y)
    use_x.add(x)

print(ans)