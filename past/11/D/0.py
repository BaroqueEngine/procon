par = [-1] * 26

def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]
    
def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)

    if x == y:
        return
    
    par[x] += par[y]
    par[y] = x

N = int(input())
for _ in range(N):
    u, v = input().split()
    u = ord(u) - ord("a")
    v = ord(v) - ord("a")
    unite(u, v)

S = input()
T = input()

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    u = ord(S[i]) - ord("a")
    v = ord(T[i]) - ord("a")
    if not same(u, v):
        print("No")
        exit()
print("Yes")