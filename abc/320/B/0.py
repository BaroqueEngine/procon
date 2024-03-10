S = input()


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


ans = 1
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        if is_palindrome(S[i: j + 1]):
            ans = max(ans, j - i + 1)
print(ans)
