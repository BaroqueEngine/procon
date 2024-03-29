N, A, B = map(int, input().split())
state = []

for i in range(N + 1):
    if i - A >= 0 and not state[i - A]:
        state.append(True)
    elif i - B >= 0 and not state[i - B]:
        state.append(True)
    else:
        state.append(False)

print("First" if state[N] else "Second")
