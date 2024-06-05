N = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))

print(sum(map(lambda x: P[x - 1], A)))
