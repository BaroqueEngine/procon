N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

route = [1]
seen = set([1])
loop_start_num = None
loop_start_index = None

while True:
    cur = route[-1]
    next = A[cur]
    if next in seen:
        loop_start_num = next
        loop_start_index = route.index(next)
        break
    seen.add(next)
    route.append(next)

if K < loop_start_index:
    print(route[K])
    exit()
K -= loop_start_index
mod = len(route) - loop_start_index
K %= mod
print(route[loop_start_index + K])
