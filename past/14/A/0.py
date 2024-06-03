N, S, T = map(int, input().split())

is_alice = (S == 0)
while N > 1:
    is_alice = not is_alice
    N -= 1

if is_alice == (T == 0):
    print("Alice")
else:
    print("Bob")
