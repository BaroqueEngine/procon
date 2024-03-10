N = int(input())
S = input()
st = set()

for i in range(N):
    st.add(S[i])
    if len(st) == 3:
        print(i + 1)
        exit()
