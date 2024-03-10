blocks = []
for _ in range(3):
    block = [input() for _ in range(4)]
    blocks.append(block)


def compression(block):
    left = 100
    right = -1
    top = 100
    bottom = -1
    for y in range(4):
        for x in range(4):
            if block[y][x] == "#":
                left = min(left, x)
                right = max(right, x)
                top = min(top, y)
                bottom = max(bottom, y)

    new_block = []
    for y in range(top, bottom + 1):
        new_block.append(block[y][left:right+1])
    return new_block


for i in range(3):
    blocks[i] = compression(blocks[i])


def rotate(block):
    w = len(block[0])
    h = len(block)

    new_block = [list(" " * h) for _ in range(w)]
    for y in range(h):
        for x in range(w):
            new_block[x][h - 1 - y] = block[y][x]

    for i in range(w):
        new_block[i] = "".join(new_block[i])

    return new_block


def width(block):
    return len(block[0])


def height(block):
    return len(block)


def fill(board, block, sx, sy):
    for y in range(height(block)):
        for x in range(width(block)):
            if block[y][x] == "#":
                if board[sy + y][sx + x] == "#":
                    return False
                board[sy + y][sx + x] = "#"
    return True


def all_filled(board):
    ok = True
    for y in range(4):
        for x in range(4):
            if board[y][x] != "#":
                ok = False
    return ok


for i in range(4):
    blocks[0] = rotate(blocks[0])
    for j in range(4):
        blocks[1] = rotate(blocks[1])
        for k in range(4):
            blocks[2] = rotate(blocks[2])

            for a in range(4 - height(blocks[0]) + 1):
                for b in range(4 - width(blocks[0]) + 1):
                    for c in range(4 - height(blocks[1]) + 1):
                        for d in range(4 - width(blocks[1]) + 1):
                            for e in range(4 - height(blocks[2]) + 1):
                                for f in range(4 - width(blocks[2]) + 1):
                                    board = [list("." * 4) for _ in range(4)]
                                    if not fill(board, blocks[0], b, a):
                                        continue
                                    if not fill(board, blocks[1], d, c):
                                        continue
                                    if not fill(board, blocks[2], f, e):
                                        continue
                                    if all_filled(board):
                                        print("Yes")
                                        exit()
print("No")
