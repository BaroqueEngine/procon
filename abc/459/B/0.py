N = int(input())
S = input().split()

dic = { "abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9}

ans = ""

for s in S:
    for k, v in dic.items():
        if s[0] in k:
            ans += str(v)

print(ans)