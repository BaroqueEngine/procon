N, M = map(int, input().split())

par = [-1] * N


def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


def same(a, b):
    return root(a) == root(b)


def merge(a, b):
    a = root(a)
    b = root(b)

    if a == b:
        return

    par[a] += par[b]
    par[b] = a


ans = 0
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if same(A, B):
        ans += 1
    else:
        merge(A, B)

print(ans)
