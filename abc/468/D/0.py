S = input()

# 奇数の回文の場合
odd_cnt = 0

for i in range(len(S)):
    left = right = i
    ng_cnt = 0
    while 0 <= left and right < len(S) and ng_cnt <= 1:
        if S[left] == S[right]:
            odd_cnt += 1
        elif ng_cnt == 0:
            odd_cnt += 1
            ng_cnt += 1
        else:
            ng_cnt += 1

        left -= 1
        right += 1

# 偶数の回文の場合
even_cnt = 0

for i in range(len(S) - 1):
    left = i
    right = i + 1
    ng_cnt = 0
    while 0 <= left and right < len(S) and ng_cnt <= 1:
        if S[left] == S[right]:
            even_cnt += 1
        elif ng_cnt == 0:
            even_cnt += 1
            ng_cnt += 1
        else:
            ng_cnt += 1

        left -= 1
        right += 1

print(odd_cnt + even_cnt)