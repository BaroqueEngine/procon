import sys
sys.setrecursionlimit(10**7)

def f(pos, dice, S, memo):
    if pos != -1 and memo[pos] != -1:
        return memo[pos]
    if pos == len(S) - 1:
        return True
    for x in dice:
        new_pos = pos + x
        if S[new_pos] == "1":
            memo[new_pos] = 0
            continue
        new_dice = dice[:]
        new_dice.remove(x)
        if f(new_pos, new_dice, S, memo):
            memo[new_pos] = 1
            return True
    memo[pos] = 0
    return False

ans = []
def solve():
    N = int(input())
    S = input()
    dice = []
    for i in range(N):
        dice.append(2**i)
    memo = [-1] * (2**N)
    ans.append("Yes" if f(-1, dice, S, memo) else "No")

T = int(input())
for _ in range(T):
    solve()

for x in ans:
    print(x)