S = input()
st = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        st.add(S[i:j])

print(len(st))
