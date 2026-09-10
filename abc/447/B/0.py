from collections import Counter
S = input()
cnt = Counter(S)
max_cnt = max(cnt.values())

print("".join(c for c in S if cnt[c] != max_cnt))