N, Q = map(int, input().split())
A = [0] * (N + 1)

strings = [list("")]
prev = [-1]

for _ in range(Q):
    T = input().split()
    T[0] = int(T[0])
    T[1] = int(T[1])
    if T[0] == 1:
        A[T[1]] = A[0]
    elif T[0] == 2:
        strings.append(list(T[2][::-1]))
        prev.append(A[T[1]])
        A[T[1]] = len(strings) - 1
    else:
        A[0] = A[T[1]]

ans = []
cur = A[0]
while prev[cur] != -1:
    ans += strings[cur]
    cur = prev[cur]

print("".join(ans[::-1]))
