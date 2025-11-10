X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

st = set([])
ans = []

for _ in range(Q):
    P = int(input())
    if P in st:
        st.remove(P)
        X -= W[P - 1]
    else:
        st.add(P)
        X += W[P - 1]
    ans.append(X)

for x in ans:
    print(x)