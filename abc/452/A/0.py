gothec = {(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)}

M, D = map(int, input().split())
print("Yes" if (M, D) in gothec else "No")