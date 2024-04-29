S = ".###..#..###.###.#.#.###.###.###.###.###.\n.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.\n.#.#..#..###.###.###.###.###...#.###.###.\n.#.#..#..#.....#...#...#.#.#...#.#.#...#.\n.###.###.###.###...#.###.###...#.###.###."
S = S.split("\n")
numbers = []

for i in range(10):
    num = []
    for y in range(5):
        x = i * 4
        num.append(S[y][x:x+4])
    numbers.append(num)

N = int(input())
T = [input() for _ in range(5)]

ans = ""
for i in range(N):
    num = []
    for y in range(5):
        x = i * 4
        num.append(T[y][x:x+4])
    for i in range(10):
        if numbers[i] == num:
            ans += str(i)
            break
print(ans)
