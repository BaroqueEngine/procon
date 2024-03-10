N, D = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

seen = [False] * N
seen[0] = True
waited = [0]

def f(x1, y1, x2, y2, D):
   dx = x1 - x2
   dy = y1 - y2

   return dx * dx + dy * dy <= D ** 2

while len(waited) > 0:
   target = waited.pop()
   for i in range(N):
      if target == i or seen[i]:
         continue
      
      if f(P[target][0], P[target][1], P[i][0], P[i][1], D):
         seen[i] = True
         waited.append(i)

for x in seen:
   print("Yes" if x else "No")