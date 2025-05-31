N = int(input())
A = sorted(list(set(map(int, input().split()))))
print(len(A))
print(*A)