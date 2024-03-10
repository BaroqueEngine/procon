N, M = map(int, input().split())
price = []
func = []

for _ in range(N):
    A = list(map(int, input().split()))
    price.append(A[0])
    func.append(A[2:])

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if price[i] < price[j]:
            continue
        ok = True
        for f in func[i]:
            if f not in func[j]:
                ok = False
                break
        if not ok:
            continue

        a = price[i] > price[j]
        b = False
        for f in func[j]:
            if f not in func[i]:
                b = True
                break
        if not (a or b):
            continue
        print("Yes")
        exit()
print("No")
