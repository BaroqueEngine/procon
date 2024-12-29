K = int(input())
S = input()
T = input()


def yes():
    print("Yes")
    exit()


def no():
    print("No")
    exit()


if abs(len(S) - len(T)) >= 2:
    no()

if len(S) == len(T):
    diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff += 1

    if diff <= 1:
        yes()
    else:
        no()

if len(S) == len(T) + 1:
    diff = 0
    i, j = 0, 0
    while i < len(S) and j < len(T):
        if S[i] != T[j]:
            diff += 1
            i += 1
        else:
            i += 1
            j += 1
    if diff <= 1:
        yes()
    else:
        no()

if len(S) + 1 == len(T):
    diff = 0
    i, j = 0, 0
    while i < len(S) and j < len(T):
        if S[i] != T[j]:
            diff += 1
            j += 1
        else:
            i += 1
            j += 1
    if diff <= 1:
        yes()
    else:
        no()
