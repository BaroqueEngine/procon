N = int(input())
powers = []
p = 1
while len(str(p)) <= 10:
    powers.append(str(p))
    p *= 2

st = set()

def dfs(result):
    if result:
        if int(result) in st:
            return
        st.add(int(result))
    if len(result) >= 10:
        return
    for tok in powers:
        if len(result) + len(tok) <= 9:
            dfs(result + tok)

dfs("")
arr = sorted(list(st), key=int)

print(arr[N - 1])
