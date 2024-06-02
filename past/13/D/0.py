N, M = map(int, input().split())
S = input()

cards = [0] * N
turn = 0
bahuda = 0

for card in S:
    cards[turn] += 1
    if card == "+":
        cards[turn] += bahuda
        bahuda = 0
    elif card == "-":
        bahuda += cards[turn]
        cards[turn] = 0
    turn = (turn + 1) % N

for card in cards:
    print(card)
