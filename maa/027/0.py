def sort(arr):
    if len(arr) <= 1:
        return arr

    size = len(arr) // 2
    a = sort(arr[:size])
    b = sort(arr[size:])
    size_a = len(a)
    size_b = len(b)

    ret = []
    i = 0
    j = 0

    while i < size_a or j < size_b:
        if i == size_a:
            ret.append(b[j])
            j += 1
        elif j == size_b:
            ret.append(a[i])
            i += 1
        else:
            if a[i] <= b[j]:
                ret.append(a[i])
                i += 1
            else:
                ret.append(b[j])
                j += 1

    return ret


N = int(input())
A = list(map(int, input().split()))
print(*sort(A))
