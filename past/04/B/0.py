X, Y = map(int, input().split())
if Y == 0:
    print("ERROR")
    exit()
P, Q = str(X / Y).split(".")
if len(Q) < 2:
    Q = Q.ljust(2, "0")
else:
    Q = Q[:2]
print("{}.{}".format(P, Q))