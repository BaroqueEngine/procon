N = int(input())
S = [input() for _ in range(N)]


def is_kaibun(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


for i in range(N):
    for j in range(i + 1, N):
        if is_kaibun(S[i] + S[j]) or is_kaibun(S[j] + S[i]):
            print("Yes")
            exit()
print("No")
