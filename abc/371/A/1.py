A, B, C = 0, 0, 0
ops = input().split()

if ops[0] == "<":
    B += 1
else:
    A += 1

if ops[1] == "<":
    C += 1
else:
    A += 1

if ops[2] == "<":
    C += 1
else:
    B += 1

if A == 1:
    print("A")
elif B == 1:
    print("B")
else:
    print("C")
