Q = int(input())


def parent(pos):
    return (pos - 1) // 2


def left(pos):
    return pos * 2 + 1


def right(pos):
    return pos * 2 + 2


def heappush(heap, x):
    heap.append(x)
    pos = len(heap) - 1
    while pos > 0 and heap[parent(pos)] > heap[pos]:
        heap[parent(pos)], heap[pos] = heap[pos], heap[parent(pos)]
        pos = parent(pos)


def heappop(heap):
    if len(heap) == 0:
        return

    last_value = heap.pop()

    if len(heap) == 0:
        return

    heap[0] = last_value
    pos = 0

    while True:
        # 子がない場合
        if left(pos) >= len(heap):
            break
        # 左右に子がある場合
        elif right(pos) < len(heap):
            if heap[left(pos)] <= heap[right(pos)]:
                if heap[left(pos)] >= heap[pos]:
                    break
                heap[left(pos)], heap[pos] = heap[pos], heap[left(pos)]
                pos = left(pos)
            else:
                if heap[right(pos)] >= heap[pos]:
                    break
                heap[right(pos)], heap[pos] = heap[pos], heap[right(pos)]
                pos = right(pos)
        # 左だけ子がある場合
        elif right(pos) >= len(heap):
            if heap[left(pos)] >= heap[pos]:
                break
            heap[left(pos)], heap[pos] = heap[pos], heap[left(pos)]
            pos = left(pos)


heap = []

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        heappush(heap, int(query[1]))
    elif query[0] == "2":
        print(heap[0])
    else:
        heappop(heap)
