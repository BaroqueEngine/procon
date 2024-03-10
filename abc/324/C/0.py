N, T = input().split()
N = int(N)


def f(s):
    if s == T:
        return True
    if abs(len(s) - len(T)) >= 2:
        return False
    if len(s) == len(T):
        error = 0
        for i in range(len(s)):
            if s[i] != T[i]:
                error += 1
                if error == 2:
                    break
        return error == 1
    elif len(s) > len(T):
        i = 0
        j = 0
        error = 0
        while j < len(T):
            if s[i] != T[j]:
                j -= 1
                error += 1
                if error == 2:
                    break
            i += 1
            j += 1
        return error <= 1
    else:
        i = 0
        j = 0
        error = 0
        while i < len(s):
            if s[i] != T[j]:
                i -= 1
                error += 1
                if error == 2:
                    break
            i += 1
            j += 1
        return error <= 1


ans = []
for i in range(1, N + 1):
    if f(input()):
        ans.append(i)

print(len(ans))
print(*ans)
