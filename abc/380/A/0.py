S = input()

for i in range(1, 4):
    if S.count(str(i)) != i:
        print("No")
        exit()
print("Yes")
