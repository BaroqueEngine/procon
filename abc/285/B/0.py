N = int(input())
S = input()

for i in range(1, N):
    cnt = 0
    for j in range(100000000):
        if j + i >= N:
            break
        if S[j] == S[j + i]:
            break
        cnt += 1
    print(cnt)
