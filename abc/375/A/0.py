N = int(input())
S = input()
words = "#.#"

ans = 0
for i in range(N - len(words) + 1):
    if S[i:i+len(words)] == words:
        ans += 1
print(ans)
