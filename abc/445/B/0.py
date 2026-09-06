N = int(input())
G = [input() for _ in range(N)]

max_len = max([len(s) for s in G])
for s in G:
    dot_len = (max_len - len(s)) // 2
    dot = "." * dot_len
    print(f"{dot}{s}{dot}")