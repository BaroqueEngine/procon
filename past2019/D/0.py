N = int(input())
dic = {}
for i in range(1, N + 1):
    dic[i] = 0
for _ in range(N):
    X = int(input())
    dic[X] += 1

x = None
y = None

for i in range(1, N + 1):
    if dic[i] == 0:
        x = i
    if dic[i] == 2:
        y = i

if x is None:
    print("Correct")
else:
    print("{} {}".format(y, x))
