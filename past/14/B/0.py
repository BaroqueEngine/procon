D = int(input())
A = int(input().replace(".", ""))
B = int(input().replace(".", ""))
C = str(A + B)
dot_pos = len(C) - D
print("{}.{}".format(C[:dot_pos], C[dot_pos:]))
