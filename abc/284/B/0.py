T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    print(sum([x % 2 == 1 for x in A]))
