N, A, B = map(int, input().split())
D = list(map(int, input().split()))
for i in range(N):
    D[i] = (D[i] - 1) % (A + B)


def diff1(D):
    return max(D) - min(D) + 1


def diff2(D):
    D = sorted(D)
    base = 0
    max_diff = 0
    for i in range(N - 1):
        diff = D[i + 1] - D[i] - 1
        if diff > max_diff:
            max_diff = diff
            base = D[i + 1]

    for i in range(N):
        D[i] = (D[i] - base) % (A + B)

    return max(D) - min(D) + 1


print("Yes" if min(diff1(D), diff2(D)) <= A else "No")
