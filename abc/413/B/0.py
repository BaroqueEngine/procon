N = int(input())
S = [input() for _ in range(N)]
st = set([])

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        T = S[i] + S[j]
        st.add(T)

print(len(st))