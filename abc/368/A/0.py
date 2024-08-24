N, T, A = map(int, input().split())

if T == A:
    print("No")
elif max(T, A) > N // 2:
    print("Yes")
else:
    print("No")
