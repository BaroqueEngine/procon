import sys
sys.setrecursionlimit(10**7)

A = [list(map(int, input().split())) for _ in range(3)]
INF = 10**18


def is_same(arr):
    return len(set(arr)) == 1


def is_game_end(seen):
    end = False
    for line in seen:
        end |= is_same(line) and line[0] != None
    for line in zip(*seen):
        end |= is_same(line) and line[0] != None
    for line in [[seen[0][0], seen[1][1], seen[2][2]]]:
        end |= is_same(line) and line[0] != None
    for line in [[seen[0][2], seen[1][1], seen[2][0]]]:
        end |= is_same(line) and line[0] != None
    return end


def f(seen, turn, score):
    if is_game_end(seen):
        return INF if turn % 2 == 1 else -INF
    if turn == 9:
        return score[0] - score[1]

    best_score = -INF if turn % 2 == 0 else INF

    for y in range(3):
        for x in range(3):
            if seen[y][x] == None:
                seen[y][x] = turn % 2
                score[turn % 2] += A[y][x]
                cur_score = f(seen, turn + 1, score)
                if turn % 2 == 0:
                    best_score = max(best_score, cur_score)
                else:
                    best_score = min(best_score, cur_score)
                seen[y][x] = None
                score[turn % 2] -= A[y][x]
    return best_score


best_score = f([[None] * 3 for _ in range(3)], 0, [0, 0])
print("Takahashi" if best_score > 0 else "Aoki")
