T = int(input())

def solve():
    N = int(input())
    weights = 0
    powers = 0
    num = N
    A = []
    for _ in range(N):
        W, P = map(int, input().split())
        A.append((W, P))
        weights += W
    A.sort(key=lambda x: x[0] + x[1])
    while len(A) > 0 and weights > powers:
        W, P = A.pop()
        num -= 1
        weights -= W
        powers += P

    return num

ans = []
for _ in range(T):
    ans.append(solve())

for x in ans:
    print(x)