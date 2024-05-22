X, Y = map(int, input().split())

def divide_num(x):
    ret = 0
    for i in range(1, x + 1):
        if i * i > x:
            break
        if x % i == 0:
            ret += 1
            if i * i != x:
                ret += 1
    return ret

x_num = divide_num(X)
y_num = divide_num(Y)

if x_num == y_num:
    print("Z")
elif x_num > y_num:
    print("X")
else:
    print("Y")