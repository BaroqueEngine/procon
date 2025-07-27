N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

A = []

def f(depth, arr):
    if depth == K:
        A.append(arr)
        return
    for i in range(1, N + 1):
        f(depth + 1, arr + [i])
f(0, [])
words = []
for arr in A:
    word = []
    for i in arr:
        word.append(S[i - 1])
    words.append("".join(word))

words.sort()
print(words[X - 1])