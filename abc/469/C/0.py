N = int(input())
S = input()

ans = []
hit = 0

for i in range(N):
    while hit + len(ans) + 1 <= 0 and len(ans) < N:
        ans.append(i)

    hit -= 1

    if S[i] == "o":
        hit += 1

while len(ans) < N:
    ans.append(N)

for x in ans:
    print(x)