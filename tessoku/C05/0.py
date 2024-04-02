N = int(input())
N -= 1

s = bin(N)[2:].zfill(10)
s = s.replace("0", "4").replace("1", "7")
print(s)