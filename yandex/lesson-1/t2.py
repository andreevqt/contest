sides = []
sides.append(int(input()))
sides.append(int(input()))
sides.append(int(input()))

exists = False
for i in range(len(sides)):
  sum = 0
  for j in range(len(sides)):
    if j != i:
      sum += sides[j]
  exists = sides[i] < sum
  if not exists:
    break

if exists:
  print("YES")
else:
  print("NO")
