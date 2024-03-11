class List:
    def __init__(self, value, prev, next) -> None:
        self.value = value
        self.prev = prev
        self.next = next


N = int(input())
A = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[A[i]] = List(A[i], None, None)


def erase(x):
    cur = dic[x]
    prev = cur.prev
    next = cur.next
    prev.next = next
    next.prev = prev
    del dic[x]


def add(x, y):
    cur = dic[x]
    next_next = cur.next
    next = List(y, None, None)
    dic[y] = next
    cur.next = next
    next.prev = cur
    next.next = next_next
    next_next.prev = next


head = List(-1, None, None)
tail = List(-1, None, None)
first = List(A[0], head, tail)
dic[A[0]] = first
head.next = first
tail.prev = first


def print_list():
    cur = head.next
    values = []
    while cur != tail:
        values.append(cur.value)
        cur = cur.next
    print(*values)


for i in range(1, N):
    add(A[i - 1], A[i])

Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        add(q[1], q[2])
    else:
        erase(q[1])

print_list()
