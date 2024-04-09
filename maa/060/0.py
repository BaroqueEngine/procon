# 00 = L
# 01 = W
# 02 = W
# 03 = W
# 04 = L
# 05 = W
# 06 = W
# 07 = W
# 08 = L
# 09 = W
# 10 = W

dic = {
    "W": "First",
    "L": "Second"
}

N = int(input())
print(dic["LWWW"[N % 4]])
