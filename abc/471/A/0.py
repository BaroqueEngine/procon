A, B = map(int, input().split())
ans = [A + B, A - B, A * B, A / B]
print("Nine" if 9 in ans else "Nein")