A = [
    ["A", "B", "C"],
    ["A", "C", "B"],
    ["B", "A", "C"],
    ["B", "C", "A"],
    ["C", "A", "B"],
    ["C", "B", "A"],
]

orders = ["AB", "AC", "BC"]

ops = input().split()

for arr in A:
    ok = True
    for i in range(3):
        order = orders[i]
        if ops[i] == "<":
            if arr.index(order[0]) >= arr.index(order[1]):
                ok = False
        else:
            if arr.index(order[0]) <= arr.index(order[1]):
                ok = False
    if ok:
        print(arr[1])
        exit()
