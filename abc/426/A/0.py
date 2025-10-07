dic = {
    "Ocelot": 0,
    "Serval": 1,
    "Lynx": 2
}

X, Y = input().split()

print("Yes" if dic[X] >= dic[Y] else "No")