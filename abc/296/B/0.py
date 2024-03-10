for y in range(8, 0, -1):
    line = input()
    if line.count("*") > 0:
        x = line.index("*")
        print(chr(ord("a") + x) + str(y))
        exit()
