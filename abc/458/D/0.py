import heapq

X = int(input())
Q = int(input())

left = []
right = []
ans = []

for _ in range(Q):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A

    if A <= X and B <= X:
        heapq.heappush(right, X)
        heapq.heappush(left, -A)
        heapq.heappush(left, -B)
        X = -heapq.heappop(left)
    elif A > X and B > X:
        heapq.heappush(left, -X)
        heapq.heappush(right, A)
        heapq.heappush(right, B)
        X = heapq.heappop(right)
    else:
        heapq.heappush(left, -A)
        heapq.heappush(right, B)

    ans.append(X)

for x in ans:
    print(x)    