N, M = map(int, input().split())
S = input()
T = input()

head = False
tail = False

if T[:N] == S:
    head = True
if T[-N:] == S:
    tail = True

if head and tail:
    print(0)
elif head and not tail:
    print(1)
elif not head and tail:
    print(2)
else:
    print(3)
