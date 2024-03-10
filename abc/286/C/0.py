from collections import deque

N, A, B = map(int, input().split())
S = deque(list(input()))

ans = 100000000000000000


def kaibun_missed_count(s):
    cnt = 0
    left = 0
    right = len(S) - 1
    while left < right:
        if s[left] != s[right]:
            cnt += 1
        left += 1
        right -= 1
    return cnt


for i in range(N):
    ans = min(ans, i * A + kaibun_missed_count(S) * B)
    S.append(S.popleft())

print(ans)
