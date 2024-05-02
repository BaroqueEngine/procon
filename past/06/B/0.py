S = input()
pos = S.find("post")
if pos == -1:
    print("none")
else:
    print(pos // 4 + 1)