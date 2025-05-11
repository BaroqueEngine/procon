N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

def check():
    S = set(A)
    for i in range(1, M + 1):
        if i not in S:
            return True
    return False

while not check():
    A.pop()
    cnt += 1

print(cnt)