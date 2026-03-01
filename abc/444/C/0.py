N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = []

def check_pair(arr, x):
    if len(arr) % 2 != 0:
        return False
    
    ok = True
    for i in range(len(arr) // 2):
        if arr[i] + arr[-(i + 1)] != x:
            ok = False
    if not ok:
        return False
    return True

# 全部ペアの場合
if check_pair(A, A[0] + A[-1]):
    ans.append(A[0] + A[-1])

# 一番大きい値がLだった場合
B = A[:]
while len(B) > 0 and B[-1] == A[-1]:
    B.pop()
if len(B) > 0:
    if check_pair(B, A[-1]):
        ans.append(A[-1])
else:
    ans.append(A[0])

print(*sorted(list(set(ans))))

