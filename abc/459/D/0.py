# 2文字 => 1文字までOK
# 3文字 => 2文字までOK
# 4文字 => 2文字までOK
# 5文字 => 3文字までOK
# 6文字 => 3文字までOK

from collections import defaultdict
import heapq
T = int(input())
ans = []
for _ in range(T):
    S = input()
    dic = defaultdict(int)
    max_cnt = 0
    for c in S:
        dic[c] += 1
        max_cnt = max(max_cnt, dic[c])
    if max_cnt > (len(S) + 2 - 1) // 2: # (a + b - 1) // b
        ans.append("No")
    else:
        ans.append("Yes")
        q = []
        for k, v in dic.items():
            heapq.heappush(q, (-v, k))

        ans_str = []
        while len(q) > 0:
            if len(q) == 1:
                v, k = heapq.heappop(q)
                ans_str.append(k)
            else:
                v0, k0 = heapq.heappop(q)
                v1, k1 = heapq.heappop(q)
                v0 = -v0
                v1 = -v1
                ans_str.append(k0)
                ans_str.append(k1)
                v0 -= 1
                v1 -= 1

                if v0 > 0:
                    heapq.heappush(q, (-v0, k0))
                if v1 > 0:
                    heapq.heappush(q, (-v1, k1))

        ans.append("".join(ans_str))

for x in ans:
    print(x)
