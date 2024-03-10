N, M, H, K = map(int, input().split())
S = input()
A = [list(map(int, input().split())) for _ in range(M)]
P = set()

for a in A:
    P.add((a[0], a[1]))

items = dict()
for p in P:
  items[p] = True

hp = H
x, y = 0, 0
for dir in S:
   if dir == "R":
      x += 1
   elif dir == "L":
      x -= 1
   elif dir == "U":
      y += 1
   else:
      y -= 1
   
   hp -= 1
   if hp < 0:
      print("No")
      exit()

   if (x, y) in items and items[(x, y)] and hp < K:
      items[(x, y)] = False
      hp = K

print("Yes")

