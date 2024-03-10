N = int(input())
st = set()
pair = set()
cnt = 0

for _ in range(N):
    S = input()
    RS = S[::-1]

    if S not in st and RS not in st:
        cnt += 1

    st.add(S)
    st.add(RS)

print(cnt)
