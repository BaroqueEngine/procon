A, B, C, D, R = map(int, input().split())
rec = [False] * (2010)

time = 0
start = A
end = A + R
while True:
    if time >= B:
        start = C
        end = C + R
    if time > end:
        break
    for i in range(max(time, start), end):
        rec[i] = True
    time += D

for i in range(C, C + R):
    if not rec[i]:
        print("No")
        exit()
print("Yes")
