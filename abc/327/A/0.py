N = int(input())
S = input()

print("Yes" if S.count("ab") > 0 or S.count("ba") > 0 else "No")
