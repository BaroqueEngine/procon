N = int(input())
S = [input() for _ in range(N)]

if all(map(lambda x: x == "Perfect", S)):
    print("All Perfect")
elif all(map(lambda x: x in ["Perfect", "Great"], S)):
    print("Full Combo")
else:
    print("Failed")
