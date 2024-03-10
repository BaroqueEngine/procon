N, K = map(int, input().split())

K -= N + N - 2
if K < 0:
    print("No")
    exit()

if K % 2 == 0:
    print("Yes")
else:
    print("No")
