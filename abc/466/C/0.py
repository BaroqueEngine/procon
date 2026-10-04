N = int(input())

ans = 0
j = 2
for i in range(1, N + 1):
    j = max(j, i + 1)
    while j < N + 1:
        print(f"? {i} {j}", flush=True)
        yes = input() == "Yes"
        if yes:
            j += 1
        else:
            break
    ans += j - i - 1

print(f"! {ans}")