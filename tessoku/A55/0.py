st = set()

import bisect

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        st.add(query[1])
    elif query[0] == 2:
        st.remove(query[1])
    else:
        arr = list(st)
        arr.sort()
        pos = bisect.bisect_left(arr, query[1])
        if len(arr) <= pos:
            print(-1)
        else:
            print(arr[pos])

# NG
