import sys
import queue
sys.setrecursionlimit(10**7)

N = int(input())
S = input() + ".."
T = input() + ".."

dic = {}
dic[S] = 0
P = set()
P.add(S)
q = queue.Queue()
q.put((S, len(S) - 2, 0, S))

while not q.empty():
    str, dot_pos, cnt, prev_str = q.get()

    for i in range(N + 2 - 1):
        if str[i] == "." or str[i + 1] == ".":
            continue
        next_str = list(str[::])
        pattern = next_str[i:i+2]
        next_str[i:i+2] = ".."
        next_str[dot_pos:dot_pos+2] = pattern
        next_str = "".join(next_str)
        if next_str in P:
            continue
        P.add(next_str)
        dic[next_str] = cnt + 1
        q.put((next_str, i, cnt + 1, str))

if T in P:
    print(dic[T])
else:
    print(-1)
