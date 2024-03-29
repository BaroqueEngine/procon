dic = {
    "W": 0,
    "B": 1,
    "R": 2
}

N, C = input().split()
N = int(N)
A = input()

ans = 0
for c in A:
    ans += dic[c]

print("Yes" if ans % 3 == dic[C] else "No")
