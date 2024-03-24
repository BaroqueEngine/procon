W, B = map(int, input().split())
N = W + B

base = "wbwbwwbwbwbw"
S = base * 30

for i in range(len(S) - N + 1):
    str = S[i:i+N]
    if str.count("w") == W and str.count("b") == B:
        print("Yes")
        exit()
print("No")
