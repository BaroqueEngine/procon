N = int(input())
S = input()

tak = S.count("T")
aoki = S.count("A")

if tak > aoki:
    print("T")
elif tak < aoki:
    print("A")
elif S[-1] == "A":
    print("T")
else:
    print("A")