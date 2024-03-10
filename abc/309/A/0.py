dic = {}
dic[1] = [2]
dic[2] = [1, 3]
dic[3] = [2]
dic[4] = [5]
dic[5] = [4, 6]
dic[6] = [5]
dic[7] = [8]
dic[8] = [7, 9]
dic[9] = [8]

A, B = map(int, input().split())
print("Yes" if B in dic[A] else "No")
