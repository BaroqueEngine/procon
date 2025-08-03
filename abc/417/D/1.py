import sys
sys.setrecursionlimit(10**7)

ans = []

def solve():
    N, M, X, Y = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].append(B)
        G[B].append(A)

    for g in G:
        g.sort()

    path = []
    visited = [False] * (N + 1)

    def dfs(cur):
        path.append(cur)
        visited[cur] = True

        if cur == Y:
            ans.append(path)
            return True

        for next in G[cur]:
            if not visited[next]:
                if dfs(next):
                    return True
        
        path.pop()
        
        return False

    dfs(X)

T = int(input())
for _ in range(T):
    solve()

for x in ans:
    print(*x)

